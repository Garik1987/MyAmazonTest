from selenium.webdriver.common.by import By
from Sources.Base.basePage import BasePage

class ProfilesPageLocator():
    profilesPageLocator = (By.XPATH, '(//*[@class="a-spacing-none ya-card__heading--rich a-text-normal"])[7]')


class ProfilesPage (ProfilesPageLocator, BasePage):
    def __init__(self, driver):
       self.driver = driver
       super().__init__(driver)

    def profiles_page (self):
        profilesPage = self.find_element(*(self.profilesPageLocator))
        profilesPage.click()

