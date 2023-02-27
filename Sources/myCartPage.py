from selenium.webdriver.common.by import By
from Sources.basePage import BasePage

class MyCartPageLocator():
    myCartPageLocator = (By.ID, "nav-cart-count-container")
    removeItemFromCartLocator = (By.XPATH, '//*[@name="submit.delete.C61c30455-885b-4eba-9cb9-a6d441a53b50"]')

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