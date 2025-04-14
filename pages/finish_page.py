import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Finish_page(Base):
    """Класс Finish_page отвечает за завершение пользовательской сессии (выход из личного кабинета)
        на сайте https://zurmarket.ru/. Наследуется от базового класса Base.

        Атрибуты класса:
            url (str): URL главной страницы сайта.

        Методы класса разделены на три логические группы:
        1. Getters — методы, возвращающие элементы на странице с ожиданием их кликабельности или видимости.
        2. Actions — действия, производимые с элементами (клик).
        3. Methods — сложные действия, объединяющие несколько базовых (например, выход из аккаунта)."""

    url = 'https://zurmarket.ru/'

    # ===== LOCATORS =====

    personal_office_logo = "//div[@class='personal top login twosmallfont']"
    personal_office = "//h1[contains (text(), 'Личный кабинет')]"
    getout = "(//a[@href='/?logout=yes&login=yes'])[2]"
    start_login = "//span[contains (text(), 'Войти')]"

    # ===== GETTERS =====

    def get_personal_office_logo(self):
        """Ожидает и возвращает логотип/иконку личного кабинета."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.personal_office_logo)))

    def get_personal_office(self):
        """Ожидает и возвращает заголовок 'Личный кабинет'."""
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.personal_office)))

    def get_getout_button(self):
        """Ожидает и возвращает кнопку выхода из аккаунта."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.getout)))

    def get_start_login_button(self):
        """Ожидает и возвращает кнопку 'Войти' на главной странице (после выхода)."""
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.start_login)))

    # ===== ACTIONS =====

    def click_personal_office_logo(self):
        """Кликает по иконке личного кабинета."""
        self.get_personal_office_logo().click()
        print("Click personal office logo")

    def click_get_out_button(self):
        """Кликает по кнопке 'Выйти'."""
        self.get_getout_button().click()
        print("Click get out button")

    # ===== METHODS =====

    def finish(self):
        """Полный сценарий завершения сессии:
            - открывает сайт,
            - переходит в личный кабинет,
            - проверяет наличие заголовка 'Личный кабинет',
            - выходит из аккаунта,
            - проверяет появление кнопки 'Войти',
            - проверяет URL после выхода."""
        with allure.step("Finish"):
            Logger.add_start_step(method="finish")
            self.driver.get(self.url)
            self.get_current_url()
            self.click_personal_office_logo()
            self.assert_word(self.get_personal_office(), 'Личный кабинет')
            self.click_get_out_button()
            self.assert_word(self.get_start_login_button(), 'Войти')
            self.assert_url('https://zurmarket.ru/?login=yes')
            Logger.add_end_step(url=self.driver.current_url, method="finish")
