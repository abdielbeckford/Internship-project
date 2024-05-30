from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open the main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@when('Log in to the page')
def login(context):
    context.app.main_page.sign_in()
    context.app.main_page.click_continue()


@when('Click on settings option')
def click_settings(context):
    context.app.home_page.click_settings()


@when('Click on Contact us option')
def click_contact_us(context):
    context.app.settings_page.click_contact_us()


@then('Verify the right page opens')
def verify_contact_page(context):
    context.app.contact_us_page.verify_contact_page()


@then('Verify there are at least {amount} social media icons')
def verify_social_media_icons(context, amount):
    context.app.contact_us_page.verify_social_media_icons(amount)
