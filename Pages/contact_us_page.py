from Pages.base_page import Page
from selenium.webdriver.common.by import By


class ContactUsPage(Page):
    sm_icons = (By.CSS_SELECTOR, "a.contact-button")

    def verify_contact_page(self):
        self.verify_url('https://soft.reelly.io/contact-us')

    def verify_social_media_icons(self, expected_amount):
        expected_amount = int(expected_amount)
        sm_icons = self.find_elements(*self.sm_icons)
        assert len(sm_icons) >= expected_amount, f"Expected {expected_amount} elements, but found {len(sm_icons)}"
