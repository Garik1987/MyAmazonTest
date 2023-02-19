from selenium.webdriver.common.by import By

class SearchResult():
    def __init__(self, driver):
        self.driver = driver

    def click_result_element(self):
        clickResultElement = self.driver.find_element(By.CLASS_NAME, "a-size-base-plus a-color-base a-text-normal")
        clickResultElement.click()
