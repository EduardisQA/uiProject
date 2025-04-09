from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Personal_page(Base):

    """Класс Personal_page отвечает за действия в личном кабинете пользователя на сайте https://zurmarket.ru/.
    Наследуется от базового класса Base, в котором реализованы универсальные методы взаимодействия с элементами.

    Атрибуты класса:
        url (str): URL страницы личного кабинета.

    Логическая структура класса:
    1. Locators — локаторы всех разделов личного кабинета, кнопок отмены заказа и других элементов управления.
    2. Getters — методы ожидания появления элементов для взаимодействия.
    3. Actions — методы действий: клики по разделам, кнопкам отмены заказа, переходы по меню.
    4. Methods — сценарные методы для комплексной работы со страницей.

    Основные возможности:
        - Отмена текущего заказа с подтверждением причины отмены.
        - Переход по всем разделам личного кабинета: Личные данные, История заказов, Профили заказов, Корзина, Подписки, Контакты.
        - Проверка корректности переходов через assert на заголовках страниц."""

    url = 'https://zurmarket.ru/personal/'

    def __init__(self, driver):
        """Конструктор класса. Принимает веб-драйвер Selenium."""
        super().__init__(driver)
        self.driver = driver

    # ===== LOCATORS =====
    # (XPath локаторы для кнопок навигации, заголовков страниц и элементов управления в личном кабинете)

    current_orders = "//h2[contains (text(), 'Текущие заказы')]"
    my_orders = "//h1[@id='pagetitle']"
    cancel_order = "//a[contains (text(), 'Отменить заказ')]"
    order_cancellation_radio_button = "//input[@value='Неудобна точка самовывоза']"
    confirmation_cancel_order = "//input[@value='Отменить заказ']"
    personal_data = "//h2[contains (text(), 'Личные данные')]"
    user_profile = "//h1[@id='pagetitle']"
    order_history = "//h2[contains (text(), 'История заказов')]"
    my_orders_history = "//h1[@id='pagetitle']"
    my_office_button = "(//a[@href='/personal/index.php'])[2]"
    order_profiles = "//h2[contains (text(), 'Профили заказов')]"
    profiles = "//h1[@id='pagetitle']"
    cart = "//h2[contains (text(), 'Корзина')]"
    inside_cart = "//h1[@id='pagetitle']"
    subscriptions = "//h2[contains (text(), 'Подписки')]"
    your_subscriptions = "//h1[@id='pagetitle']"
    contacts = "//h2[contains (text(), 'Контакты')]"
    your_contacts = "//h1[@id='pagetitle']"

    # ===== GETTERS =====
    # (Методы ожидания загрузки и получения элементов личного кабинета)

    def get_current_orders(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.current_orders)))

    def get_my_orders_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.my_orders)))

    def get_cancel_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cancel_order)))

    def get_order_cancellation_radio_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_cancellation_radio_button)))

    def get_confirmation_cancel_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirmation_cancel_order)))

    def get_personal_data(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.personal_data)))

    def get_user_profile_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_profile)))

    def get_order_history(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_history)))

    def get_my_orders_history_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.my_orders_history)))

    def get_my_office_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.my_office_button)))

    def get_order_profiles(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_profiles)))

    def get_profiles_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profiles)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_inside_cart_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.inside_cart)))

    def get_subscriptions(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.subscriptions)))

    def get_your_subscriptions_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.your_subscriptions)))

    def get_contacts(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.contacts)))

    def get_your_contacts_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.your_contacts)))

    # ===== ACTIONS =====
    # (Методы кликов по различным разделам и кнопкам действий в личном кабинете)

    def click_current_orders(self):
        self.get_current_orders().click()
        print("Click current orders")

    def click_cancel_order(self):
        self.get_cancel_order().click()
        print("Click cancel order")

    def click_order_cancellation_radio_button(self):
        self.get_order_cancellation_radio_button().click()
        print("Click order cancellation radio-button")

    def click_confirmation_cancel_order(self):
        self.get_confirmation_cancel_order().click()
        print("Click confirmation cancel order")

    def click_personal_data(self):
        self.get_personal_data().click()
        print("Click personal data")

    def click_order_history(self):
        self.get_order_history().click()
        print("Click order history")

    def click_my_office_button(self):
        self.get_my_office_button().click()
        print("Click my office button")

    def click_order_profiles(self):
        self.get_order_profiles().click()
        print("Click order profiles")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    def click_subscriptions(self):
        self.get_subscriptions().click()
        print("Click subscriptions")

    def click_contacts(self):
        self.get_contacts().click()
        print("Click contacts")

    # ===== HELPERS =====

    def go_back_to_personal_page(self):
        """Возвращает пользователя на страницу личного кабинета."""
        self.driver.back()
        print("Return to personal page")

    # ===== METHODS =====

    def personal_information(self):
        """Полный сценарий проверки разделов личного кабинета:
            - Отмена заказа;
            - Переход по основным разделам с проверкой заголовков."""
        self.driver.get(self.url)
        self.get_current_url()

        # 1. Отмена заказа
        self.click_current_orders()
        self.assert_word(self.get_my_orders_word(), 'Мои заказы')
        self.click_cancel_order()
        self.click_order_cancellation_radio_button()
        self.click_confirmation_cancel_order()

        self.driver.get(self.url)
        self.get_current_url()

        # 2. Личные данные
        self.click_personal_data()
        self.assert_word(self.get_user_profile_word(), 'Профиль пользователя')
        self.go_back_to_personal_page()

        # 3. История заказов
        self.click_order_history()
        self.assert_word(self.get_my_orders_history_word(), 'Мои заказы')
        self.go_back_to_personal_page()

        # 4. Профили заказов
        self.click_my_office_button()
        self.click_order_profiles()
        self.assert_word(self.get_profiles_word(), 'Профили')
        self.go_back_to_personal_page()

        # 5. Корзина
        self.click_cart()
        self.assert_word(self.get_inside_cart_word(), 'Корзина')
        self.go_back_to_personal_page()

        # 6. Подписки
        self.click_subscriptions()
        self.assert_word(self.get_your_subscriptions_word(), 'Ваши подписки')
        self.go_back_to_personal_page()

        # 7. Контакты
        self.click_contacts()
        self.assert_word(self.get_your_contacts_word(), 'Контакты')
        self.go_back_to_personal_page()