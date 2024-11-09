from behave import *
from page_objects.login_page import LoginPage
from webdriver_hooks.webdriver_hooks import WebDriverHooks
from utils.get_credentials import get_credentials
# from blender import Blender


@given(u'I am on the Youtube main page')
def step_impl(context):
    # WebDriverHooks().set_driver()
    # context.driver = WebDriverHooks().get_driver()
    #
    # credentials = get_credentials()
    # user_name = credentials[0]
    # password = credentials[1]
    #
    # LoginPage(context.driver, user_name, password)
    pass


@given(u'I click on Sign In')
def step_impl(context):
    pass


@when(u'I enter "{invalid_email}" and click Next')
def step_impl(context, invalid_email):
    # context.blender = Blender()
    # context.blender.add(invalid_email)
    print(f"Invalid email: {invalid_email}")


@then(u'I verify if an error message containing "{error_message}" is displayed')
def step_impl(context, error_message):
    print(f"Error message: {error_message}")


@given(u'I click on Sign In and select my account')
def step_impl(context):
    pass


@when(u'I enter a valid email')
def step_impl(context):
    pass


@when(u'I click Next')
def step_impl(context):
    pass


@then(u'I enter a valid password')
def step_impl(context):
    pass


@then(u'I click Next')
def step_impl(context):
    pass


@then(u'I verify that I am successfully logged in')
def step_impl(context):
    pass


@then(u'I log out')
def step_impl(context):
    pass


@then(u'I close the browser')
def step_impl(context):
    pass

