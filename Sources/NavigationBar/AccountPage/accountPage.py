from selenium.webdriver.common.by import By
from Sources.Base.basePage import BasePage

class AccountPageLocator():
    accountPageLocator = (By.ID, "nav-link-accountList-nav-line-1")

class AccountPage (AccountPageLocator, BasePage):
    def __init__(self, driver):
       self.driver = driver
       super().__init__(driver)

    def account_page (self):
        accountPage = self.find_element(*(self.accountPageLocator))
        accountPage.click()

