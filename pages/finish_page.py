from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Finish_page(Base):

    url = 'https://zurmarket.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    personal_office_logo = "//div[@class='personal top login twosmallfont']"
    personal_office = "//h1[contains (text(), 'Личный кабинет')]"
    getout = "(//a[@href='/?logout=yes&login=yes'])[2]"
    start_login = "//span[contains (text(), 'Войти')]"

    # Getters

    def get_personal_office_logo(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.personal_office_logo)))

    def get_personal_office(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.personal_office)))

    def get_getout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.getout)))

    def get_start_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.start_login)))

    # Actions

    def click_personal_office_logo(self):
        self.get_personal_office_logo().click()
        print("Click personal office logo")

    def click_get_out_button(self):
        self.get_getout_button().click()
        print("Click get out button")

    # Methods

    def finish(self):
        self.driver.get(self.url)
        self.get_current_url()
        self.click_personal_office_logo()
        self.assert_word(self.get_personal_office(), 'Личный кабинет')
        self.click_get_out_button()
        self.assert_word(self.get_start_login_button(), 'Войти')
        self.assert_url('https://zurmarket.ru/?login=yes')
