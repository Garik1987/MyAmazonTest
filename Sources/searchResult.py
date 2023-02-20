from selenium.webdriver.common.by import By

class SearchResult():
    def __init__(self, driver):
        self.driver = driver

    def click_search_result(self):
        searchResultElement = self.driver.find_element(By.LINK_TEXT, "https://www.amazon.com/adidas-Racer-Adapt-Running-Black/dp/B0812K6KBF/ref=sr_1_3?crid=17HC8VY800PV9&keywords=adidas&qid=1676903607&sprefix=adidas%2Caps%2C466&sr=8-3")
        searchResultElement.click()