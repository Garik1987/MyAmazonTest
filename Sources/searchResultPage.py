from selenium.webdriver.common.by import By

class MyFirstProductLocators():
    clickMyFirstProductLocators = (By.XPATH, '(//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"])[4]')

class MyFirstProduct(MyFirstProductLocators):
    def __init__(self, driver):
        self.driver = driver

    def click_my_first_product(self):
        myFirstProductElement = self.driver.find_element(*(self.clickMyFirstProductLocators))
        myFirstProductElement.click()


