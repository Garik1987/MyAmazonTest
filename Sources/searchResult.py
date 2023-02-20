from selenium.webdriver.common.by import By

class ClickSearchLocators():
    clickSearchResultLocators = (By.ID, '(//div[@class="sg-col-inner"])[4]')

class SearchResult(ClickSearchLocators):
    def __init__(self, driver):
        self.driver = driver

    def click_search_result(self):
        searchResultElement = self.driver.find_element(*(self.clickSearchResultLocators))
        searchResultElement.click()