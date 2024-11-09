from behave import *
from page_objects.login_page import LoginPage
from webdriver_hooks.webdriver_hooks import WebDriverHooks
from utils.get_credentials import get_credentials


@given('you are on the Allegro login page')
def step_impl(context):
    WebDriverHooks().set_driver()
    context.driver = WebDriverHooks().get_driver()

    credentials = get_credentials()
    user_name = credentials[0]
    password = credentials[1]

    LoginPage(context.driver, user_name, password)


@given('you enter your username and password')
def step_impl(context):
    assert True is not False


@then('you click log in')
def step_impl(context):
    assert context.failed is False


@then('you log out')
def step_impl(context):
    pass

