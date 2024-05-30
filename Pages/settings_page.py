from Pages.base_page import Page
from selenium.webdriver.common.by import By


class SettingsPage(Page):
    contact_us_btn = (By.XPATH, "//div[text()='Contact us' and @class='setting-text']")

    def click_contact_us(self):
        self.click(*self.contact_us_btn)
