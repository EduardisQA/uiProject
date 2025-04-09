from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PriceVerifier:

    def __init__(self, driver):
        self.driver = driver

    def verify_price_doubling(self, unit_price_locator, plus_button_locator, total_price_locator):
        wait = WebDriverWait(self.driver, 20)

        unit_price_element = wait.until(EC.visibility_of_element_located((By.XPATH, unit_price_locator)))
        unit_price_text = unit_price_element.text.replace('₽', '').replace(' ', '').strip()
        unit_price = int(unit_price_text)

        expected_total = unit_price * 2

        plus_button = wait.until(EC.element_to_be_clickable((By.XPATH, plus_button_locator)))
        plus_button.click()

        expected_total_text = f"{expected_total:,} ₽".replace(",", " ")

        wait.until(EC.text_to_be_present_in_element((By.XPATH, total_price_locator), expected_total_text))

        actual_total_element = wait.until(EC.visibility_of_element_located((By.XPATH, total_price_locator)))
        actual_total_text = actual_total_element.text.replace('₽', '').replace(' ', '').strip()
        actual_total = int(actual_total_text)

        assert actual_total == expected_total, f"Ожидали: {expected_total}, получили: {actual_total}"
        print(f"Цена удвоилась корректно: {actual_total}₽")
