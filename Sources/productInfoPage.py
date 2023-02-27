from selenium.webdriver.common.by import By
from Sources.basePage import BasePage

class ProductInfoPageLocators():
    addToCardLocators = (By.ID, "add-to-cart-button")
class ProductInfoPage(ProductInfoPageLocators, BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)


    def click_add_to_cart_button(self):
        addToCartelement = self.find_element(*(self.addToCardLocators))
        addToCartelement.click()
