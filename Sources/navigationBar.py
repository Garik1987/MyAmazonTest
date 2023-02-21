from selenium.webdriver.common.by import By


class NavigationBarLocators():
    searchFildLocators = (By.ID, "twotabsearchtextbox")
    clickSearchButtonElementLocators = (By.ID, "nav-search-submit-button")

class NavigationBar(NavigationBarLocators):
    def __init__(self, driver):
        self.driver = driver

    def fill_search_fild(self, text):
        searchFildElement = self.driver.find_element(*(self.searchFildLocators))
        searchFildElement.clear()
        searchFildElement.send_keys(text)

    def click_search_button_element(self):
        clickSearchButtonElement = self.driver.find_element(*(self.clickSearchButtonElementLocators))
        clickSearchButtonElement.click()
