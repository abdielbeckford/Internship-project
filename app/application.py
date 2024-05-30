from Pages.base_page import Page
from Pages.main_page import MainPage
from Pages.home_page import HomePage
from Pages.settings_page import SettingsPage
from Pages.contact_us_page import ContactUsPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.home_page = HomePage(driver)
        self.settings_page = SettingsPage(driver)
        self.contact_us_page = ContactUsPage(driver)
