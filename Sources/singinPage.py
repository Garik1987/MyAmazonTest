from selenium.webdriver.common.by import By

class SingInPageLocators():
    loginFiledLocators = (By.ID, "ap_email")
    continueButtonLocators = (By.ID, "continue")
    passwordFildElementLocators = (By.ID, "ap_password")
    singInButtonElementLocators = (By.ID, "signInSubmit")

class SingInPage(SingInPageLocators):
    def __init__(self, driver):
        self.driver = driver


    def fill_login_field(self, login):
        loginFildElement = self.driver.find_element(*(self.loginFiledLocators))
        loginFildElement.clear()
        loginFildElement.send_keys(login)

    def click_to_continue_button (self):
        continueButtonElement = self.driver.find_element(*(self.continueButtonLocators))
        continueButtonElement.click()

    def fill_password_field(self, password):
        passwordFildElement = self.driver.find_element(*(self.passwordFildElementLocators))
        passwordFildElement.clear()
        passwordFildElement.send_keys(password)

    def click_to_singin_button(self):
        singinButtonElement = self.driver.find_element(*(self.singInButtonElementLocators))
        singinButtonElement.click()
