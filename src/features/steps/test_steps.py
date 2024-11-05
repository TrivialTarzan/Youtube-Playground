from behave import *


@given('there was no scenario')
def there_was_no_scenario(context):
    pass


@when('there was no real need to have any')
def step_impl(context):
    assert True is not False


@then('I added one')
def step_impl(context):
    assert context.failed is False


@when('I felt I had to')
def step_impl(context):
    pass



