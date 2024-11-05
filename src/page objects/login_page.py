import selenium
from seleniumpagefactory import PageFactory

class LoginPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        'user_name': ('name', "login"),
        'password': ('name', 'password'),
        'login_btn': ('button', 'submit')
    }
