from selenium.webdriver.common.by import By

class MainMenuPageLocator():
    mainMenuPageLocator = (By.ID, "nav-logo-sprites")
class MainMenuPage(MainMenuPageLocator):
    def __init__(self, driver):
        self.driver = driver

    def main_menu_page(self):
        mainMenuPage = self.driver.find_element(*(self.mainMenuPageLocator))
        mainMenuPage.click()
