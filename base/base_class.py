import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Methot GET current URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url {get_url}")

    """Methot assert word"""

    def assert_word(self, element, expected_text):
        actual_text = element.text.strip()
        assert expected_text in actual_text, f"Ожидали, что '{expected_text}' будет в '{actual_text}'"
        print(f"Good value word: найдено '{expected_text}' в '{actual_text}'")

    """Methot assert price"""

    def assert_price(self, price, result):
        """Проверяет равенство двух ценовых значений."""
        value_price = price.text.strip() if hasattr(price, 'text') else str(price).strip()
        value_result = result.text.strip() if hasattr(result, 'text') else str(result).strip()
        assert value_price == value_result, f"Ожидали цену '{value_result}', но получили '{value_price}'"
        print("Good value price")

    # """Methot Screenshot"""
    #
    # def get_screenshot(self):
    #     now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
    #     name_screenshot = 'screenshot' + now_date + '.png'
    #     self.driver.save_screenshot('/Users/e.shaihulov/PycharmProjects/main_ui/screen/' + name_screenshot)

    """Methot assert url"""

    def assert_url(self, exp_result):
        get_url = self.driver.current_url
        assert get_url == exp_result
        print("Good value url")

    def wait_for_overlay_to_disappear(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "jqmOverlay")))
            print("Overlay disappeared")
        except TimeoutException:
            print("Overlay всё ещё висит — продолжаем")

    """Method: Click with retry to handle stale element"""

    def click_with_retry(self, by, value, timeout=10, retries=2):
        last_exception = None
        for attempt in range(retries):
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable((by, value))
                )
                element.click()
                print(f"Clicked element on attempt {attempt + 1}: {value}")
                return
            except StaleElementReferenceException as e:
                print(f"[Retry {attempt + 1}] StaleElementReferenceException, retrying...")
                last_exception = e
            except TimeoutException as e:
                print(f"[Retry {attempt + 1}] TimeoutException waiting for element: {value}")
                last_exception = e
        raise last_exception
