from selenium.webdriver.common.by import By

class ProductInfoPageLocators():
    addToCardLocators = (By.ID, "add-to-cart-button")
class ProductInfoPage(ProductInfoPageLocators):
    def __init__(self, driver):
        self.driver = driver


    def click_add_to_cart_button(self):
        addToCartelement = self.driver.find_element(*(self.addToCardLocators))
        addToCartelement.click()
