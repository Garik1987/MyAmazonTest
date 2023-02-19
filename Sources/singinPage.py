from selenium.webdriver.common.by import By

class SingInPage():
    def __init__(self, driver):
        self.driver = driver


    def fill_login_field(self, login):
        loginFildElement = self.driver.find_element(By.ID, "ap_email")
        loginFildElement.clear()
        loginFildElement.send_keys(login)

    def click_to_continue_button (self):
        continueButtonElement = self.driver.find_element(By.ID, "continue")
        continueButtonElement.click()

    def fill_password_field(self, password):
        passwordFildElement = self.driver.find_element(By.ID, "ap_password")
        passwordFildElement.clear()
        passwordFildElement.send_keys(password)

    def click_to_singin_button(self):
        singinButtonElement = self.driver.find_element(By.ID, "signInSubmit")
        singinButtonElement.click()
