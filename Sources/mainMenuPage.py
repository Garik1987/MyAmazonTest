from selenium.webdriver.common.by import By


class MainMenuLocators():
    mainMenuButtonElementLocators = (By.CLASS_NAME, "nav-logo-link nav-progressive-attribute")


class MainMenuPage(MainMenuLocators):
    def __init__(self, driver):
        self.driver = driver

    def main_menu_button(self):
        mainMenuButtonElement = self.driver.find_element(*(self.mainMenuButtonElementLocators))
        mainMenuButtonElement.click()
