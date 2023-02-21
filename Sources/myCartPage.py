from selenium.webdriver.common.by import By

class MyCartPageLocator():
    myCartPageLocator = (By.ID, "nav-cart-count-container")


class MyCartPage(MyCartPageLocator):
    def __init__(self, driver):
       self.driver = driver

    def my_cart_page(self):
        myCartPage = self.driver.find_element(*(self.myCartPageLocator))
        myCartPage.click()
