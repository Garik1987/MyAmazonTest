from selenium.webdriver.common.by import By

class MyCartPageLocator():
    myCartPageLocator = (By.ID, "nav-cart-count-container")
    removeItemFromCartLocator = (By.XPATH, '//*[@name="submit.delete.C61c30455-885b-4eba-9cb9-a6d441a53b50"]')

class MyCartPage(MyCartPageLocator):
    def __init__(self, driver):
       self.driver = driver

    def my_cart_page(self):
        myCartPage = self.driver.find_element(*(self.myCartPageLocator))
        myCartPage.click()

    def remove_item_from_cart(self):
        removeItemFromCart = self.driver.find_element(*(self.removeItemFromCartLocator))
        removeItemFromCart.click()