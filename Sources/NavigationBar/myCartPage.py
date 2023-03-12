from selenium.webdriver.common.by import By
from Sources.Base.basePage import BasePage

class MyCartPageLocator():
    myCartPageLocator = (By.ID, "nav-cart-count-container")
    removeItemFromCartLocator = (By.XPATH, "(//input[@data-action='delete'])[1]")

class MyCartPage(MyCartPageLocator, BasePage):
    def __init__(self, driver):
       self.driver = driver
       super().__init__(driver)

    def my_cart_page(self):
        myCartPage = self.find_element(*(self.myCartPageLocator))
        myCartPage.click()

    def remove_item_from_cart(self):
        removeItemFromCart = self.find_element(*(self.removeItemFromCartLocator))
        removeItemFromCart.click()