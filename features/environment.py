from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application


def browser_init(context, scenario_name):
    """
    :param scenario_name: name of the scenario
    :param context: Behave context
    """

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)
    #
    # options = webdriver.FirefoxOptions()
    #
    # options.add_argument('headless')
    # options.add_argument('--window-size=1920,1080')

    bs_user = 'abdielrodriguezb_1pxPRh'
    bs_key = 'nTq3tFr2abJ2qWLv38w2'
    url = f"http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub"

    options = Options()
    bstack_options = {
        'os': 'Windows',
        'osVersion': '10',
        'browserName': 'Firefox',
        'sessionName': scenario_name
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    # context.driver.maximize_window()
    # context.driver.maximize_window()
    context.driver.set_window_size(1920, 1080)
    context.driver.implicitly_wait(4)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
