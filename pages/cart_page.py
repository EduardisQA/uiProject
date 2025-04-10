import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger
from utilities.price_verifier import PriceVerifier


class Cart_page(Base):

    """Класс Cart_page отвечает за взаимодействие с корзиной на сайте https://zurmarket.ru/.
    Наследуется от базового класса Base, где реализованы общие методы (например, assert_word, click_with_retry и др.).

    Атрибуты класса:
        url (str): URL главной страницы сайта (откуда переходим в корзину).
        product_name (str): Название выбранного товара для проверки в корзине.
        product_price (str): Цена выбранного товара для проверки в корзине.

    Методы класса логически разделены на три блока:
    1. Locators — пути к элементам страницы (XPath локаторы).
    2. Getters — методы ожидания и получения элементов.
    3. Actions — действия с элементами (клики).
    4. Methods — полноценные пользовательские сценарии проверки корзины.

    Ключевые функции:
        - Подтверждение наличия выбранного товара в корзине.
        - Проверка удвоения стоимости при увеличении количества товара.
        - Передача информации о товаре для последующих проверок на странице оформления заказа."""

    url = 'https://zurmarket.ru/'

    def __init__(self, driver, product_name, product_price):
        """Конструктор класса. Принимает веб-драйвер Selenium и ожидаемые название и цену товара."""
        super().__init__(driver)
        self.driver = driver
        self.product_name = product_name
        self.product_price = product_price

    # ===== LOCATORS =====
    # (XPath пути ко всем элементам корзины: иконка корзины, название товара, цена и пр.)

    icon_cart = "(//i[@class='svg inline  svg-inline-basket big'])[1]"
    product_name_locator = "//a[@class='basket-item-info-name-link']"
    product_price_locator = "(//div[@class='basket-item-price-current'])[1]"
    add_one_more_item = "//span[@class='basket-item-amount-btn-plus']"
    amount_after_doubling = "(//span[@class='basket-item-price-current-text'])[2]"
    total_price_value = "//div[@class='basket-coupon-block-total-price-current']"
    place_order_button = "//button[@class='btn btn-lg btn-default basket-btn-checkout white']"
    compare_page_title = "//h1[@id='pagetitle']"

    # ===== GETTERS =====
    # (Методы для получения элементов с явным ожиданием)

    def get_icon_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.icon_cart)))

    def get_product_name_element(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_name_locator)))

    def get_product_price_element(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_price_locator)))

    def get_add_one_more_item(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_one_more_item)))

    def get_amount_after_doubling(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.amount_after_doubling)))

    def get_total_price_value(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_price_value)))

    def get_place_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.place_order_button)))

    def get_compare_page_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.compare_page_title)))

    # ===== ACTIONS =====
    # (Методы, реализующие клики по элементам корзины)

    def click_icon_cart(self):
        self.get_icon_cart().click()
        print("Click icon cart")

    def click_add_one_more_item(self):
        self.get_add_one_more_item().click()
        print("Click add one more item")

    def click_place_order_button(self):
        self.get_place_order_button().click()
        print("Click place order button")

    # ===== METHODS =====
    # (Сценарные методы для автоматизации полного процесса работы с корзиной)

    def product_confirmation(self):
        """Полный сценарий проверки товара в корзине:
            - Открытие корзины;
            - Проверка названия и цены товара;
            - Проверка удвоения стоимости при увеличении количества;
            - Переход к оформлению заказа;
            - Возвращение информации о товаре для дальнейших проверок."""
        with allure.step("Product confirmation"):
            Logger.add_start_step(method="product_confirmation")
            self.driver.get(self.url)
            self.get_current_url()
            self.click_icon_cart()
            self.assert_word(self.get_product_name_element(), self.product_name)
            self.assert_price(self.get_product_price_element(), self.product_price)
            self.verify_price_double()

            cart_product_info = self.get_cart_product_info()

            self.click_place_order_button()
            self.assert_word(self.get_compare_page_title(), 'Оформление заказа')
            Logger.add_end_step(url=self.driver.current_url, method="product_confirmation")
        return cart_product_info

    def verify_price_double(self):
        verifier = PriceVerifier(self.driver)
        verifier.verify_price_doubling(
            unit_price_locator=self.product_price_locator,
            plus_button_locator=self.add_one_more_item,
            total_price_locator=self.amount_after_doubling
        )

        updated_total_price_element = self.get_total_price_value()
        updated_amount_after_doubling_element = self.get_amount_after_doubling()

        self.assert_price(updated_total_price_element, updated_amount_after_doubling_element)

    def get_cart_product_info(self):
        """Возвращает информацию о товаре в корзине (название, цена за единицу, итоговая цена) в виде словаря."""
        return {
            "name": self.get_product_name_element().text,
            "unit_price": self.get_product_price_element().text,
            "total_price": self.get_amount_after_doubling().text
        }