from selenium.webdriver.common.by import By

class MyFirstProductLocators():
    clickMyFirstProductLocators = (By.XPATH, '(//span[@class="a-size-medium a-color-base a-text-normal"])[1]')

class MyFirstProduct(MyFirstProductLocators):
    def __init__(self, driver):
        self.driver = driver

    def click_my_first_product(self):
        myFirstProductElement = self.driver.find_element(*(self.clickMyFirstProductLocators))
        myFirstProductElement.click()


