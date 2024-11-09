from behave import *
from blender import Blender
from page_objects.login_page import LoginPage
from webdriver_hooks.webdriver_hooks import WebDriverHooks
from utils.get_credentials import get_credentials


@given(u'I am on the Youtube main page')
def step_impl(context):
    WebDriverHooks().set_driver()
    context.driver = WebDriverHooks().get_driver()

    credentials = get_credentials()
    user_name = credentials[0]
    password = credentials[1]

    LoginPage(context.driver, user_name, password)


@given(u'I click on Sign In')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I click on Sign In')


@when(u'I enter "{invalid_email}" and click Next')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter invalid.email@.com and click Next')


@then(u'I verify if an error message containing "{error_message}" is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I verify if an error message containing Enter a valid email is displayed')


@given(u'I click on Sign In and select my account')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I click on Sign In and select my account')


@when(u'I enter a valid email')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter a valid email')


@when(u'I click Next')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click Next')


@then(u'I enter a valid password')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I enter a valid password')


@then(u'I click Next')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I click Next')


@then(u'I verify that I am successfully logged in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I verify that I am successfully logged in')


@then(u'I log out')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I log out')


@then(u'I close the browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I close the browser')

