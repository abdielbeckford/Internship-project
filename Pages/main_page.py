from Pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    Email = (By.ID, 'email-2')
    Password = (By.ID, 'field')
    Continue_Btn = (By.CSS_SELECTOR, "a.login-button")

    def open_main_page(self):
        self.driver.get('https://soft.reelly.io/sign-in')

    def sign_in(self):
        email_field = self.find_element(*self.Email)
        email_field.send_keys('ar188966@gmail.com')
        password_field = self.find_element(*self.Password)
        password_field.send_keys('Abdiel2002!')
        # self.input_text(self.Email).send_keys('ar188966@gmail.com')
        # self.input_text(self.Password).send_keys('Abdiel2002!')

    def click_continue(self):
        self.click(*self.Continue_Btn)


