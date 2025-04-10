import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class login_page(Base):
    """
    Класс login_page отвечает за авторизацию пользователя на сайте https://zurmarket.ru/.
    Наследуется от базового класса Base, в котором реализованы общие методы (например, assert_word, click_with_retry и др.).

    Атрибуты класса:
        url (str): URL главной страницы сайта.
        name (str): Логин (e-mail) пользователя по умолчанию.
        user_password (str): Пароль пользователя по умолчанию.

    Методы класса разделены на три логические группы:
    1. Getters — методы, возвращающие элементы на странице с ожиданием их кликабельности.
    2. Actions — действия, производимые с элементами (клик, ввод и т.д.).
    3. Methods — сложные действия, объединяющие несколько базовых (например, авторизация).
    """

    url = 'https://zurmarket.ru/'
    name = 'shaihulove@yandex.ru'
    user_password = 's_yCzdD_93pvECd'

    def __init__(self, driver):
        """Конструктор класса. Принимает веб-драйвер Selenium."""
        super().__init__(driver)
        self.driver = driver

    # ===== LOCATORS =====

    start_login_button = "//span[contains (text(), 'Войти')]"
    user_name = "//input[@id='USER_LOGIN_POPUP']"
    password = "//input[@id='USER_PASSWORD_POPUP']"
    button_login = "//button[@class='btn btn-default bold']"
    button_for_check_main_word = "(//i[@class='svg inline  svg-inline-cabinet'])[1]"
    main_word = "//h1[contains(text(), 'Личный кабинет')]"

    # ===== GETTERS =====

    def get_start_login_button(self):
        """Ожидает и возвращает кнопку 'Войти' на главной странице."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.start_login_button)))

    def get_user_name(self):
        """Ожидает и возвращает поле ввода логина."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        """Ожидает и возвращает поле ввода пароля."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_login(self):
        """Ожидает и возвращает кнопку подтверждения логина."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_button_for_check_main_word(self):
        """Ожидает и возвращает иконку 'личный кабинет' (используется для проверки входа)."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_for_check_main_word)))

    def get_main_word(self):
        """Ожидает и возвращает заголовок 'Личный кабинет' (используется в assert)."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # ===== ACTIONS =====

    def click_start_login_button(self):
        """Кликает по кнопке 'Войти' на главной странице."""
        self.get_start_login_button().click()
        print("click start login button")

    def input_user_name(self, user_name):
        """Вводит логин в поле логина."""
        self.get_user_name().send_keys(user_name)
        print("input user")

    def input_password(self, password):
        """Вводит пароль в поле пароля."""
        self.get_password().send_keys(password)
        print("input password")

    def click_button_login(self):
        """Кликает по кнопке входа."""
        self.get_button_login().click()
        print("click login button")

    def click_button_for_check_main_word(self):
        """Кликает по иконке личного кабинета.
        Использует click_with_retry из базового класса для избежания ошибок типа stale element."""
        self.click_with_retry(By.XPATH, self.button_for_check_main_word)
        print("click button for check main word")

    # ===== METHODS =====

    def authorization(self):
        """Полный сценарий авторизации:
            - открывает сайт,
            - кликает 'Войти',
            - вводит логин и пароль,
            - кликает кнопку входа,
            - проверяет, что вход выполнен успешно, по заголовку 'Личный кабинет'."""
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_start_login_button()
            self.input_user_name(self.name)
            self.input_password(self.user_password)
            self.click_button_login()
            self.wait_for_overlay_to_disappear()
            self.click_button_for_check_main_word()
            self.assert_word(self.get_main_word(), 'Личный кабинет')
            Logger.add_end_step(url=self.driver.current_url, method="authorization")
