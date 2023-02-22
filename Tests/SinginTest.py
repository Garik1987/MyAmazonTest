import time
from selenium import webdriver
import unittest
from Sources.singinPage import SingInPage
from Sources.navigationBar import NavigationBar
from Sources.searchResultPage import MyFirstProduct
from Sources.productInfoPage import ProductInfoPage
from Sources.myCartPage import MyCartPage
from Sources.mainMenuPage import MainMenuPage

class MyTest (unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
        self.singInPageObj = SingInPage(self.driver)
        self.searchButtonObj = NavigationBar(self.driver)
        self.myFirstProductObj = MyFirstProduct(self.driver)
        self.addToCartObj = ProductInfoPage(self.driver)
        self.myCartPageObj = MyCartPage(self.driver)
        self.mainMenuPageObj = MainMenuPage(self.driver)
    def test_singin(self):
        self.singInPageObj.fill_login_field("garikarakelyan32@gmail.com")
        self.singInPageObj.click_to_continue_button()
        time.sleep(6)
        self.singInPageObj.fill_password_field("gar092270")
        self.singInPageObj.click_to_singin_button()
        self.searchButtonObj.fill_search_fild("Garmin Vivoactive 4")
        self.searchButtonObj.click_search_button_element()
        self.myFirstProductObj.click_my_first_product()
        self.addToCartObj.click_add_to_cart_button()
        self.myCartPageObj.my_cart_page()
        time.sleep(3)
        self.myCartPageObj.remove_item_from_cart()
        time.sleep(3)
        self.mainMenuPageObj.main_menu_button()
        time.sleep(3)

    def tearDown(self) -> None:
        self.driver.close()