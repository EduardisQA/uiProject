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
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    print("Start Test 1")

    login = login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver, mp.product_name, mp.product_price)
    cart_product_info = cp.product_confirmation()

    op = Order_page(driver)
    op.order_confirmation(cart_product_info)

    pp = Personal_page(driver)
    pp.personal_information()

    f = Finish_page(driver)
    f.finish()

    print("Finish test 1")


# # @pytest.mark.run(order=1)


def test_buy_product_2():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    print("Start Test 2")

    login = login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_2()

    cp = Cart_page(driver, mp.product_name, mp.product_price)
    cart_product_info = cp.product_confirmation()

    op = Order_page(driver)
    op.order_confirmation(cart_product_info)

    pp = Personal_page(driver)
    pp.personal_information()

    f = Finish_page(driver)
    f.finish()

    print("Finish test 2")


# # @pytest.mark.run(order=2)


def test_buy_product_3():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    print("Start Test 3")

    login = login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_3()

    cp = Cart_page(driver, mp.product_name, mp.product_price)
    cart_product_info = cp.product_confirmation()

    op = Order_page(driver)
    op.order_confirmation(cart_product_info)

    pp = Personal_page(driver)
    pp.personal_information()

    f = Finish_page(driver)
    f.finish()

    print("Finish test 3")


def test_buy_product_4():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    print("Start Test 4")

    login = login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_4()

    cp = Cart_page(driver, mp.product_name, mp.product_price)
    cart_product_info = cp.product_confirmation()

    op = Order_page(driver)
    op.order_confirmation(cart_product_info)

    pp = Personal_page(driver)
    pp.personal_information()

    f = Finish_page(driver)
    f.finish()

    print("Finish test 4")


def test_buy_product_5():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    print("Start Test 5")

    login = login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_5()

    f = Finish_page(driver)
    f.finish()

    print("Finish test 5")