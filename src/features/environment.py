from selenium import webdriver
from behave import fixture, use_fixture
# from behave4my_project.fixtures import wsgi_server


@fixture
def selenium_browser_chrome(context):
    context.browser = webdriver.Chrome()
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


def before_all(context):
    use_fixture(selenium_browser_chrome, context)
    # -- CLEANUP-FIXTURE is performed after after_all() hook is called.
