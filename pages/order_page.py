from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Order_page(Base):
    """Класс Order_page отвечает за работу с этапом оформления заказа на сайте https://zurmarket.ru/.
    Наследуется от базового класса Base, который предоставляет универсальные методы проверки и взаимодействия с элементами.

    Атрибуты класса:
        url (str): URL страницы оформления заказа.

    Методы класса логически разделены на блоки:
    1. Locators — локаторы элементов оформления заказа (XPath).
    2. Getters — методы ожидания загрузки и получения веб-элементов.
    3. Actions — методы для действий с элементами (например, клики).
    4. Methods — сценарные методы для полной проверки процесса оформления заказа.

    Ключевые функции:
        - Проверка правильности выбранных способа оплаты, доставки и личных данных покупателя.
        - Сравнение информации о товаре между корзиной и оформлением заказа.
        - Завершение оформления заказа.
        - Переход в личный кабинет после успешного оформления заказа."""

    url = 'https://zurmarket.ru/order/'

    def __init__(self, driver):
        """Конструктор класса. Принимает веб-драйвер Selenium."""
        super().__init__(driver)
        self.driver = driver

    # ===== LOCATORS =====
    # (XPath локаторы для поиска способов оплаты, доставки, информации о товаре и кнопок)

    payment_option = "//div[@class='bx-soa-pp-company-selected']"
    delivery_option = "//div[@class='col-sm-9 bx-soa-pp-company-selected']"
    name_locator = "//*[@id='bx-soa-properties']/div[2]/div[2]"
    email_locator = "//*[@id='bx-soa-properties']/div[2]/div[3]"
    phone_locator = "//*[@id='bx-soa-properties']/div[2]/div[4]"
    product_name_order_locator = "(//div[@class='bx-soa-item-content']//a)[1]"
    product_unit_price_order_locator = "(//div[contains(@class, 'bx-soa-item-td-text')])[2]"
    product_total_price_order_locator = "(//div[contains(@class, 'bx-soa-item-td-text')])[4]"
    place_an_order = "//a[@class='pull-right btn btn-default btn-lg hidden-xs']"
    order_is_formed = "//h1[contains (text(), 'Заказ сформирован')]"
    personal_office_button = "(//a[contains (text(), 'Личный кабинет')])[2]"
    personal_office = "//h1[contains (text(), 'Личный кабинет')]"

    # ===== GETTERS =====
    # (Методы ожидания и получения всех ключевых элементов страницы оформления заказа)

    def get_payment_option(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.payment_option)))

    def get_delivery_option(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.delivery_option)))

    def get_name_element(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.name_locator)))

    def get_email_element(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.email_locator)))

    def get_phone_element(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.phone_locator)))

    def get_product_name_order(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.product_name_order_locator)))

    def get_product_unit_price_order(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.product_unit_price_order_locator)))

    def get_product_total_price_order(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.product_total_price_order_locator)))

    def get_place_an_order(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.place_an_order)))

    def get_order_is_formed(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.order_is_formed)))

    def get_personal_office_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.personal_office_button)))

    def get_personal_office(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.personal_office)))

    # ===== ACTIONS =====
    # (Методы, реализующие клики на странице оформления заказа)

    def click_place_an_order_button(self):
        self.get_place_an_order().click()
        print("Click place an order")

    def click_personal_office_button(self):
        self.get_personal_office_button().click()
        print("Click personal office")

    # ===== METHODS =====
    # (Полный сценарий проверки оформления заказа)

    def order_confirmation(self, product_info):
        """Проверяет корректность данных оформления заказа:
            - способ оплаты;
            - способ доставки;
            - личные данные (имя, e-mail, телефон);
            - название, цена и сумма заказа;
            - оформляет заказ;
            - проверяет успешное создание заказа;
            - переходит в личный кабинет покупателя."""
        Logger.add_start_step(method="order_confirmation")
        self.driver.get(self.url)
        self.get_current_url()
        self.assert_word(self.get_payment_option(), 'Наличный расчет')
        self.assert_word(self.get_delivery_option(), 'Самовывоз по адресу пр-кт Ямашева, 45 (г. Казань)')
        self.assert_word(self.get_name_element(), 'Эдуард')
        self.assert_word(self.get_email_element(), 'shaihulove@yandex.ru')
        self.assert_word(self.get_phone_element(), '8 (950) 323-22-37')
        self.assert_word(self.get_product_name_order(), product_info["name"])
        self.assert_price(self.get_product_unit_price_order(), product_info["unit_price"])
        self.assert_price(self.get_product_total_price_order(), product_info["total_price"])
        self.click_place_an_order_button()
        self.assert_word(self.get_order_is_formed(), 'Заказ сформирован')
        self.click_personal_office_button()
        self.assert_word(self.get_personal_office(), 'Личный кабинет')
        Logger.add_end_step(url=self.driver.current_url, method="order_confirmation")
