from behave import *
from page_objects.login_page import LoginPage
from webdriver_hooks.webdriver_hooks import WebDriverHooks
from utils.get_credentials import get_credentials


@given('you are on the Allegro login page')
def navigate_to_login_page(context):
    WebDriverHooks().set_driver()
    context.driver = WebDriverHooks().get_driver()

    credentials = get_credentials()
    user_name = credentials[0]
    password = credentials[1]

    LoginPage(context.driver, user_name, password)


@then('you enter your username and password')
def enter_credentials(context):
    assert True is not False


@then('you click log in')
def log_in(context):
    assert context.failed is False


@when('you log out')
def log_out(context):
    pass

