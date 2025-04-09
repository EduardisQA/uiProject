from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.personal_office import Personal_page
from pages.finish_page import Finish_page
from pages.login_page import login_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from pages.order_page import Order_page


def test_buy_product_1(set_group):
    # Инициализация драйвера Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    print("Start Test 1")

    # Авторизация пользователя
    login = login_page(driver)
    login.authorization()

    # Выбор товара с главной страницы
    mp = Main_page(driver)
    mp.select_products_1()

    # Подтверждение добавления товара в корзину
    cp = Cart_page(driver, mp.product_name, mp.product_price)
    cart_product_info = cp.product_confirmation()

    # Оформление заказа
    op = Order_page(driver)
    op.order_confirmation(cart_product_info)

    # Проверка данных в личном кабинете
    pp = Personal_page(driver)
    pp.personal_information()

    # Завершение сценария
    f = Finish_page(driver)
    f.finish()

    print("Finish test 1")


# # @pytest.mark.run(order=1)


def test_buy_product_2():
    # Инициализация драйвера Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    print("Start Test 2")

    # Авторизация пользователя
    login = login_page(driver)
    login.authorization()

    # Выбор товара с главной страницы
    mp = Main_page(driver)
    mp.select_products_2()

    # Подтверждение добавления товара в корзину
    cp = Cart_page(driver, mp.product_name, mp.product_price)
    cart_product_info = cp.product_confirmation()

    # Оформление заказа
    op = Order_page(driver)
    op.order_confirmation(cart_product_info)

    # Проверка данных в личном кабинете
    pp = Personal_page(driver)
    pp.personal_information()

    # Завершение сценария
    f = Finish_page(driver)
    f.finish()

    print("Finish test 2")


# # @pytest.mark.run(order=2)


def test_buy_product_3():
    # Инициализация драйвера Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    print("Start Test 3")

    # Авторизация пользователя
    login = login_page(driver)
    login.authorization()

    # Выбор товара с главной страницы
    mp = Main_page(driver)
    mp.select_products_3()

    # Подтверждение добавления товара в корзину
    cp = Cart_page(driver, mp.product_name, mp.product_price)
    cart_product_info = cp.product_confirmation()

    # Оформление заказа
    op = Order_page(driver)
    op.order_confirmation(cart_product_info)

    # Проверка данных в личном кабинете
    pp = Personal_page(driver)
    pp.personal_information()

    # Завершение сценария
    f = Finish_page(driver)
    f.finish()

    print("Finish test 3")


def test_buy_product_4():
    # Инициализация драйвера Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    print("Start Test 4")

    # Авторизация пользователя
    login = login_page(driver)
    login.authorization()

    # Выбор товара с главной страницы
    mp = Main_page(driver)
    mp.select_products_4()

    # Подтверждение добавления товара в корзину
    cp = Cart_page(driver, mp.product_name, mp.product_price)
    cart_product_info = cp.product_confirmation()

    # Оформление заказа
    op = Order_page(driver)
    op.order_confirmation(cart_product_info)

    # Проверка данных в личном кабинете
    pp = Personal_page(driver)
    pp.personal_information()

    # Завершение сценария
    f = Finish_page(driver)
    f.finish()

    print("Finish test 4")


def test_buy_product_5():
    # Инициализация драйвера Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    print("Start Test 5")

    # Авторизация пользователя
    login = login_page(driver)
    login.authorization()

    # Выбор товара с главной страницы
    mp = Main_page(driver)
    mp.select_products_5()

    # Завершение сценария
    f = Finish_page(driver)
    f.finish()

    print("Finish test 5")