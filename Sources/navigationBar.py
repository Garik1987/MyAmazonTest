from selenium.webdriver.common.by import By

class NavigationBar():
    def __init__(self, driver):
        self.driver = driver

    def fill_search_fild(self, text):
        searchFildElement = self.driver.find_element(By.ID, "twotabsearchtextbox")
        searchFildElement.clear()
        searchFildElement.send_keys(text)

    def click_search_element(self):
        clickSearchElement = self.driver.find_element(By.ID, "nav-search-submit-button")
        clickSearchElement.click()
