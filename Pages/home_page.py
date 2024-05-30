from Pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(Page):
    settings_btn = (By.CSS_SELECTOR, "a.menu-button-block[href='/settings']")

    def click_settings(self):
        settings_btn = self.find_element(*self.settings_btn)
        actions = ActionChains(self.driver)
        actions.move_to_element(settings_btn)
        actions.perform()