from selenium.webdriver.common.by import By


class ProductInfoPage():
    def __init__(self, driver):
        self.driver = driver


    def click_add_to_cart_button(self):
        addToCartelement = self.driver.find_element(By.ID, "add-to-cart-button")
        addToCartelement.click()