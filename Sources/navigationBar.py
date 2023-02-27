from selenium.webdriver.common.by import By
from Sources.basePage import BasePage

class NavigationBarLocators():
    searchFildLocators = (By.ID, "twotabsearchtextbox")
    clickSearchButtonElementLocators = (By.ID, "nav-search-submit-button")

class NavigationBar(NavigationBarLocators, BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
    def fill_search_fild(self, text):
        searchFildElement = self.find_element(*(self.searchFildLocators))
        searchFildElement.clear()
        searchFildElement.send_keys(text)

    def click_search_button_element(self):
        clickSearchButtonElement = self.find_element(*(self.clickSearchButtonElementLocators))
        clickSearchButtonElement.click()
