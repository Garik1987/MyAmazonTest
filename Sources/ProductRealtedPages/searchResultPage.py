from selenium.webdriver.common.by import By
from Sources.Base.basePage import BasePage

class MyFirstProductLocators():
    clickMyFirstProductLocators = (By.XPATH, '(//span[@class="a-size-medium a-color-base a-text-normal"])[1]')

class MyFirstProduct(MyFirstProductLocators, BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
    def click_my_first_product(self):
        myFirstProductElement = self.find_element(*(self.clickMyFirstProductLocators))
        myFirstProductElement.click()


