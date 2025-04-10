import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):

    """Класс Main_page отвечает за взаимодействие с основной страницей сайта https://zurmarket.ru/.
    Наследуется от базового класса Base, в котором реализованы общие методы (например, assert_word, click_with_retry и др.).

    Атрибуты класса:
        url (str): URL главной страницы сайта.
        product_name (str): Название выбранного товара для последующей проверки.
        product_price (str): Цена выбранного товара для последующей проверки.

    Методы класса логически разделены на три блока:
    1. Locators — пути к элементам страницы (в формате XPath).
    2. Getters — методы для ожидания и получения элементов.
    3. Actions — методы для взаимодействия с элементами (клик, наведение и пр.).
    4. Methods — комплексные сценарии выбора товаров для разных тест-кейсов."""

    url = 'https://zurmarket.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.product_name = None
        self.product_price = None

    # ===== LOCATORS =====
    # (описание: хранит XPath локаторы для всех элементов страницы)

    menu_tv_audio_button = "//td[@data-id='2620054746']"
    menu_laptop_equipment_button = "//td[@data-id='1441432216']"
    menu_hover_target_lha = "//td[@data-id='3037317652']"
    menu_hover_target_sha = "//td[@data-id='2398463810']"
    menu_hover_target_other = "(//a[@class='dropdown-toggle more-items'])[1]"
    menu_hover_target_other_category_musical = "(//a[@href='/catalog/muzykalnye_instrumenty/'])[1]"
    menu_hover_category_musical_instruments_guitars = "(//a[@href='/catalog/muzykalnye_instrumenty/gitary/'])[1]"
    category_sha = "(//a[@title='Техника для дома'])[1]"
    tv = "(//a[contains(text(), 'Телевизоры')])[2]"
    monitors = "//a[contains(text(), 'Мониторы')]"
    refrigerators = "(//a[@href='/catalog/krupnaya_bytovaya_tekhnika/kholodilniki/'])[1]"
    irons = "//div[@id='bx_1847241719_1363']"
    menu_sort_by = "//div[@class='sortSelect']"
    sort_by_desc_price = "//a[contains(@href, 'sort=PRICE&order=desc') and contains(text(), 'Убыванию цены')]"
    sort_dropdown_ul = "//div[contains(@class, 'sortSelect') and contains(@class, 'active')]//ul"
    filter_price_line = "//div[@id='colorAvailableActive_e4da3b7fbbce2345d7772b0674a318d5']"
    filter_availability_in_store = "//div[@data-property_id='8271']"
    filter_manufacturer = "//div[@data-property_id='5163']"
    filter_freezer_location = "//div[@data-prop_code='raspolochkameru_h']"
    filter_compressor_quantity = "//div[@data-property_id='6095']"
    filter_refrigerator_height = "//div[@data-property_id='7995']"
    check_box_in_stock_7_10 = "//span[@title='Есть на складе (7-10 дней)']"
    check_box_in_stock_1_2 = "//span[@title='Есть на складе (1-2 дня)']"
    check_box_manufacturer_gorenge = "//span[@title='GORENJE']"
    check_box_manufacturer_econ = "//span[@title='Econ']"
    check_box_manufacturer_sigma = "//span[contains(text(), 'SIGMA')]"
    check_box_freezer_location_from_below = "//span[@title='снизу ']"
    check_box_compressor_quantity = "(//span[@title='1'])[2]"
    check_box_refrigerator_height = "//span[@title='От 200 см']"
    show_result_search_button = "//input[@id='set_filter']"
    samsung_tv = "//div[@id='bx_3966226736_492116']"
    samsung_tv_value = "(//span[contains(text(), 'Телевизор Samsung QE77S90daexru')])[1]"
    samsung_tv_price_value = "//span[contains(text(), '310 589 ₽')]"
    asus_monitor = "(//span[contains (text(), 'Монитор Asus Rog Strix Xg49vq')])[1]"
    gorenje_refrigerator = "//a[@id='bx_3966226736_460828_pict']"
    econ_iron = "//a[@id='bx_3966226736_436030_pict']"
    sigma_guitar = "//a[@id='bx_3966226736_383957_pict']"
    compare_the_name = "//h1[@id='pagetitle']"
    compare_the_availability = "//p[contains(text(), 'Нет в наличии')]"
    cart_button = "//div[@class='button_block wide']"
    monitor_value_locator = "(//a[@href='/catalog/kompyutery_noutbuki_" \
                            "orgtekhnika/monitory/monitor_asus_rog_strix_xg49vq.html'])[2]"
    monitor_price_locator = "(//span[@class='values_wrapper'])[1]"
    refrigerator_value_locator = "(//a[@href='/catalog/krupnaya_bytovaya_tekhnika/kholodilniki/kholodilnik_gorenje_nrk6201sybk.html'])[2]"
    product_price_element = "//div[@data-value='95090']"
    econ_iron_price_locator = "//span[contains (text(), '2 420 ₽')]"

    # ===== GETTERS =====
    # (описание: методы для ожидания кликабельности или видимости элементов)

    def get_menu_tv_audio_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_tv_audio_button)))

    def get_menu_laptop_equipment_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_laptop_equipment_button)))

    def get_hover_target_menu_lha(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.menu_hover_target_lha)))

    def get_hover_target_menu_sha(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.menu_hover_target_sha)))

    def get_hover_target_menu_other(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.menu_hover_target_other)))

    def get_hover_on_target_menu_other_category_musical(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.menu_hover_target_other_category_musical)))

    def get_hover_category_musical_instruments_guitars(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.menu_hover_category_musical_instruments_guitars)))

    def get_category_sha(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.category_sha)))

    def get_tv(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tv)))

    def get_monitors(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.monitors)))

    def get_refrigerators(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.refrigerators)))

    def get_irons(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.irons)))

    def get_menu_sort_by(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_sort_by)))

    def get_sort_dropdown_links(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.sort_dropdown_ul)))
        return self.driver.find_elements(By.XPATH, f"{self.sort_dropdown_ul}//a")

    def get_filter_price_line(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_line)))

    def get_filter_availability_in_store(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_availability_in_store)))

    def get_filter_manufacturer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_manufacturer)))

    def get_filter_freezer_location(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_freezer_location)))

    def get_filter_compressor_quantity(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_compressor_quantity)))

    def get_filter_refrigerator_height(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_refrigerator_height)))

    def get_check_box_manufacturer_gorenge(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_manufacturer_gorenge)))

    def get_check_box_manufacturer_econ(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_manufacturer_econ)))

    def get_check_box_manufacturer_sigma(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_manufacturer_sigma)))

    def get_check_box_in_stock_7_10(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_in_stock_7_10)))

    def get_check_box_in_stock_1_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_in_stock_1_2)))

    def get_check_box_freezer_location_from_below(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_freezer_location_from_below)))

    def get_check_box_compressor_quantity(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_compressor_quantity)))

    def get_check_box_refrigerator_height(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_refrigerator_height)))

    def get_show_result_search_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_result_search_button)))

    def get_samsung_tv(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.samsung_tv)))

    def get_samsung_tv_value(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.samsung_tv_value)))

    def get_samsung_tv_price_value(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.samsung_tv_price_value)))

    def get_asus_monitor(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.asus_monitor)))

    def get_gorenje_refrigerator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.gorenje_refrigerator)))

    def get_econ_iron(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.econ_iron)))

    def get_sigma_guitar(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sigma_guitar)))

    def get_compare_the_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.compare_the_name)))

    def get_compare_the_availability(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.compare_the_availability)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_monitor_value_element(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.monitor_value_locator)))

    def get_monitor_price_element(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.monitor_price_locator)))

    def get_refrigerator_value_element(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.refrigerator_value_locator)))

    def get_product_price_element(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_price_element)))

    def get_econ_iron_price_element(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.econ_iron_price_locator)))

    # ===== ACTIONS =====
    # (описание: методы для кликов, ховеров и других действий над элементами)

    def click_menu_tv_audio_button(self):
        self.get_menu_tv_audio_button().click()
        print("Click menu tv audio button")

    def click_menu_laptop_equipment_button(self):
        self.get_menu_laptop_equipment_button().click()
        print("Click menu laptop equipment button")

    def hover_on_target_menu_lha(self):
        element = self.get_hover_target_menu_lha()
        ActionChains(self.driver).move_to_element(element).perform()
        print("Hovered on target menu to trigger submenu lha")

    def hover_on_target_menu_sha(self):
        element = self.get_hover_target_menu_sha()
        ActionChains(self.driver).move_to_element(element).perform()
        print("Hovered on target menu to trigger submenu sha")

    def hover_on_target_menu_other(self):
        element = self.get_hover_target_menu_other()
        ActionChains(self.driver).move_to_element(element).perform()
        print("Hovered on target menu to trigger submenu other")

    def hover_on_target_menu_other_category_musical(self):
        element = self.get_hover_on_target_menu_other_category_musical()
        ActionChains(self.driver).move_to_element(element).perform()
        print("Hovered on target menu to trigger submenu other")

    def click_category_musical_instruments_guitars(self):
        self.get_hover_category_musical_instruments_guitars().click()
        print("Click category musical instruments guitars")

    def click_category_sha(self):
        self.get_category_sha().click()
        print("Click category sha")

    def click_tv(self):
        self.get_tv().click()
        print("Click tv")

    def click_monitors(self):
        self.get_monitors().click()
        print("Click monitors")

    def click_refrigerators(self):
        self.get_refrigerators().click()
        print("Click refrigerators")

    def click_irons(self):
        self.get_irons().click()
        print("Click irons")

    def click_menu_sort_by(self):
        self.get_menu_sort_by().click()
        print("Click menu sort by")

    def click_sort_by_desc_price(self):
        """Кликает на выпадающий список сортировки и выбирает сортировку по убыванию цены.
           Если сортировка не найдена — выбрасывает исключение."""
        self.get_menu_sort_by().click()
        for link in self.get_sort_dropdown_links():
            href = link.get_attribute("href")
            if href and "sort=PRICE&order=desc" in href:
                link.click()
                return
        raise Exception("Sort option 'Убыванию цены' not found")

    def adjust_filter_price_slider(self, right_offset: int):
        """Передвигает ползунок фильтра цены влево на заданное количество пикселей."""
        right_slider = self.get_filter_price_line()
        actions = ActionChains(self.driver)
        actions.click_and_hold(right_slider).move_by_offset(-abs(right_offset), 0).release().perform()
        print("Moved price filter slider left")

    def click_filter_availability_in_store(self):
        self.get_filter_availability_in_store().click()
        print("Click filter availability in store")

    def click_filter_freezer_location(self):
        self.get_filter_freezer_location().click()
        print("Click filter freezer location")

    def click_filter_manufacturer(self):
        self.get_filter_manufacturer().click()
        print("Click filter manufacturer")

    def click_filter_compressor_quantity(self):
        self.get_filter_compressor_quantity().click()
        print("Click filter compressor quantity")

    def click_filter_refrigerator_height(self):
        self.get_filter_refrigerator_height().click()
        print("Click filter refrigerator height")

    def click_check_box_in_stock_7_10(self):
        self.get_check_box_in_stock_7_10().click()
        print("Click check-box in stock 7-10 days")

    def click_check_box_in_stock_1_2(self):
        self.get_check_box_in_stock_1_2().click()
        print("Click check-box in stock 1-2 days")

    def click_check_box_freezer_location_from_below(self):
        self.get_check_box_freezer_location_from_below().click()
        print("Click check-box freezer location from below")

    def click_check_box_compressor_quantity(self):
        self.get_check_box_compressor_quantity().click()
        print("Click check-box compressor quantity")

    def click_check_box_refrigerator_height(self):
        self.get_check_box_refrigerator_height().click()
        print("Click check-box refrigerator height")

    def get_value_samsung_tv(self):
        value = self.get_samsung_tv_value().text
        print(f"TV name value: {value}")
        return value

    def get_price_value_samsung_tv(self):
        value = self.get_samsung_tv_price_value().text
        print(f"TV price value: {value}")
        return value

    def click_samsung_tv(self):
        self.get_samsung_tv().click()
        print("Click filter button")

    def click_asus_monitor(self):
        self.get_asus_monitor().click()
        print("Click asus monitor")

    def click_gorenje_refrigerator(self):
        self.get_gorenje_refrigerator().click()
        print("Click gorenje refrigerator")

    def click_econ_iron(self):
        self.get_econ_iron().click()
        print("Click econ iron")

    def click_sigma_guitar(self):
        self.get_sigma_guitar().click()
        print("Click sigma guitar")

    def click_show_result_search_button(self):
        self.get_show_result_search_button().click()
        print("Click show result search button")

    def click_check_box_manufacturer_gorenge(self):
        self.get_check_box_manufacturer_gorenge().click()
        print("Click check box manufacturer gorenge")

    def click_check_box_manufacturer_econ(self):
        self.get_check_box_manufacturer_econ().click()
        print("Click check box manufacturer econ")

    def click_check_box_manufacturer_sigma(self):
        self.get_check_box_manufacturer_sigma().click()
        print("Click check box manufacturer sigma")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click cart button")

    # ===== METHODS =====
    # (описание: готовые пользовательские сценарии выбора товаров)

    def select_products_1(self):
        """Выбирает телевизор Samsung, проверяет корректность названия и цены, добавляет товар в корзину."""
        with allure.step("Select products 1"):
            Logger.add_start_step(method="select_products_1")
            self.driver.get(self.url)
            self.get_current_url()
            self.click_menu_tv_audio_button()
            self.click_tv()
            self.click_sort_by_desc_price()
            self.product_name = self.get_value_samsung_tv()
            self.product_price = self.get_price_value_samsung_tv()
            self.assert_word(self.get_samsung_tv_value(), self.product_name)
            self.assert_price(self.get_samsung_tv_price_value(), self.product_price)
            self.click_samsung_tv()
            self.assert_word(self.get_compare_the_name(), 'Телевизор Samsung QE77S90daexru')
            self.click_cart_button()
            self.assert_url('https://zurmarket.ru/catalog/televizory_audio_'
                            'video/televizory/televizor_samsung_qe77s90daexru.html')
            Logger.add_end_step(url=self.driver.current_url, method="select_products_1")

    def select_products_2(self):
        """Выбирает монитор Xiaomi с использованием фильтра цены и производителя, добавляет товар в корзину."""
        with allure.step("Select products 2"):
            Logger.add_start_step(method="select_products_2")
            self.driver.get(self.url)
            self.get_current_url()
            self.click_menu_laptop_equipment_button()
            self.click_monitors()
            self.adjust_filter_price_slider(-20)
            self.click_filter_manufacturer()
            self.click_show_result_search_button()
            self.driver.execute_script("window.scrollTo(0, 0);")
            self.click_sort_by_desc_price()
            self.product_name = self.get_monitor_value_element().text
            self.product_price = self.get_monitor_price_element().text
            self.assert_word(self.get_monitor_value_element(), self.product_name)
            self.assert_price(self.get_monitor_price_element(), self.product_price)
            self.click_asus_monitor()
            self.assert_word(self.get_compare_the_name(), 'Монитор Asus Rog Strix Xg49vq')
            self.click_cart_button()
            self.assert_url(
                'https://zurmarket.ru/catalog/kompyutery_noutbuki_orgtekhnika/monitory/monitor_asus_rog_strix_xg49vq.html')
            Logger.add_end_step(url=self.driver.current_url, method="select_products_2")

    def select_products_3(self):
        """Выбирает холодильник Gorenje с применением нескольких фильтров (наличие, производитель, высота), добавляет в корзину."""
        with allure.step("Select products 3"):
            Logger.add_start_step(method="select_products_3")
            self.driver.get(self.url)
            self.get_current_url()
            self.hover_on_target_menu_lha()
            self.click_refrigerators()
            self.adjust_filter_price_slider(-25)
            self.click_filter_availability_in_store()
            self.click_check_box_in_stock_7_10()
            self.click_filter_manufacturer()
            self.click_check_box_manufacturer_gorenge()
            self.click_filter_freezer_location()
            self.click_check_box_freezer_location_from_below()
            self.click_filter_compressor_quantity()
            self.click_check_box_compressor_quantity()
            self.click_filter_refrigerator_height()
            self.click_check_box_refrigerator_height()
            self.click_show_result_search_button()
            self.click_gorenje_refrigerator()
            self.assert_word(self.get_compare_the_name(), 'Холодильник Gorenje Nrk6201sybk')
            self.product_name = self.get_compare_the_name().text
            self.product_price = self.get_product_price_element().text
            self.assert_price(self.get_product_price_element(), self.product_price)
            self.click_cart_button()
            self.assert_url(
                'https://zurmarket.ru/catalog/krupnaya_bytovaya_tekhnika/kholodilniki/kholodilnik_gorenje_nrk6201sybk.html')
            Logger.add_end_step(url=self.driver.current_url, method="select_products_3")

    def select_products_4(self):
        """Выбирает утюг Econ через фильтрацию по складу и производителю, добавляет товар в корзину."""
        with allure.step("Select products 4"):
            Logger.add_start_step(method="select_products_4")
            self.driver.get(self.url)
            self.get_current_url()
            self.hover_on_target_menu_sha()
            self.click_category_sha()
            self.click_irons()
            self.adjust_filter_price_slider(-5)
            self.click_filter_availability_in_store()
            self.click_check_box_in_stock_1_2()
            self.click_filter_manufacturer()
            self.click_check_box_manufacturer_econ()
            self.click_show_result_search_button()
            self.click_econ_iron()
            self.assert_word(self.get_compare_the_name(), 'Утюг Econ Eco-Bi2402')
            self.product_name = self.get_compare_the_name().text
            self.product_price = self.get_econ_iron_price_element().text
            self.assert_price(self.get_econ_iron_price_element(), self.product_price)
            self.click_cart_button()
            self.assert_url('https://zurmarket.ru/catalog/melkaya_bytovaya_tekhnika/'
                            'tekhnika_dlya_doma/utyugi_parovye_stantsii/utyug_econ_eco_bi2402.html')
            Logger.add_end_step(url=self.driver.current_url, method="select_products_4")

    def select_products_5(self):
        """Выбирает гитару Sigma из раздела музыкальных инструментов"""
        with allure.step("Select products 5"):
            Logger.add_start_step(method="select_products_5")
            self.driver.get(self.url)
            self.get_current_url()
            self.hover_on_target_menu_other()
            self.hover_on_target_menu_other_category_musical()
            self.click_category_musical_instruments_guitars()
            self.click_sort_by_desc_price()
            self.click_check_box_manufacturer_sigma()
            self.click_show_result_search_button()
            self.click_sigma_guitar()
            self.assert_word(self.get_compare_the_name(), 'Гитара Sigma Tm12-E')
            self.assert_word(self.get_compare_the_availability(), 'Нет в наличии')
            self.assert_url('https://zurmarket.ru/catalog/muzykalnye_instrumenty/gitary/gitara_sigma_tm12_e.html')
            Logger.add_end_step(url=self.driver.current_url, method="select_products_5")