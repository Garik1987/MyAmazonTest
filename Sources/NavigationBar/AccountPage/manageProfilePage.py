from selenium.webdriver.common.by import By
from Sources.Base.basePage import BasePage

class ManageProfilePageLocator():
    manageProfilePageLocator = (By.ID, "home-profile-active")

class ManageProfilePage (ManageProfilePageLocator, BasePage):
    def __init__(self, driver):
       self.driver = driver
       super().__init__(driver)

    def manage_profile_page(self):
        manageProfilePage = self.find_element(*(self.manageProfilePageLocator))
        manageProfilePage.click()
