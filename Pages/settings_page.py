from Pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



class SettingsPage(Page):
    contact_us_btn = (By.XPATH, "//div[@class='setting-text' and text()='Contact us']")
      # contact_us_btn = (By.XPATH, "//a[@href='/contact-us']")
      # contact_us_btn = (By.XPATH, "//div[text()='Contact us' and @class='setting-text']")


    def click_contact_us(self):
        contact_us_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.contact_us_btn))
        contact_us_option.click()
        # element = (WebDriverWait(self.driver, 10).
        # until(EC.visibility_of_element_located(*self.contact_us_btn)))
        # sleep(4)
        # self.driver.execute_script("arguments[0].scrollIntoView()", element)
        # element.click()
        # self.click(*self.contact_us_btn)
