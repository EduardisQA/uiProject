from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PriceVerifier:
    """Класс для проверки корректности удвоения цены товара в корзине."""

    def __init__(self, driver):
        self.driver = driver

    def verify_price_doubling(self, unit_price_locator, plus_button_locator, total_price_locator):
        """Проверяет, что после увеличения количества товара цена удваивается.
            :param unit_price_locator: XPath локатор цены за единицу товара
            :param plus_button_locator: XPath локатор кнопки увеличения количества
            :param total_price_locator: XPath локатор итоговой цены"""
        wait = WebDriverWait(self.driver, 20)

        # Получаем цену за единицу товара
        unit_price_element = wait.until(EC.visibility_of_element_located((By.XPATH, unit_price_locator)))
        unit_price_text = unit_price_element.text.replace('₽', '').replace(' ', '').strip()
        unit_price = int(unit_price_text)

        # Рассчитываем ожидаемую итоговую цену после увеличения количества до 2
        expected_total = unit_price * 2

        # Кликаем по кнопке "+"
        plus_button = wait.until(EC.element_to_be_clickable((By.XPATH, plus_button_locator)))
        plus_button.click()

        # Ожидаем отображения новой итоговой цены
        expected_total_text = f"{expected_total:,} ₽".replace(",", " ")
        wait.until(EC.text_to_be_present_in_element((By.XPATH, total_price_locator), expected_total_text))

        # Получаем фактическую итоговую цену и сравниваем с ожидаемой
        actual_total_element = wait.until(EC.visibility_of_element_located((By.XPATH, total_price_locator)))
        actual_total_text = actual_total_element.text.replace('₽', '').replace(' ', '').strip()
        actual_total = int(actual_total_text)

        # Проверка соответствия
        assert actual_total == expected_total, f"Ожидали: {expected_total}, получили: {actual_total}"
        print(f"Цена удвоилась корректно: {actual_total}₽")
