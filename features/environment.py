from selenium import webdriver
from behave import fixture, use_fixture


# @fixture
# def selenium_browser_chrome(context):
#     browser = webdriver.Chrome()
#     context.browser = browser.start_browser()
#     yield context.browser
#     # -- CLEANUP-FIXTURE PART:
#     context.browser.quit()
#
#
# def before_all(context):
#     use_fixture(selenium_browser_chrome, context)

