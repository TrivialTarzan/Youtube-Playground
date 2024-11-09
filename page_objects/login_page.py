from seleniumpagefactory import PageFactory


class LoginPage(PageFactory):

    def __init__(self, driver, user_name, password):
        super().__init__()
        self.driver = driver
        self.user_name = user_name
        self.password = password

    locators = {
        'user_name_input': ('name', "login"),
        'password_input': ('name', 'password'),
        'login_btn': ('button', 'submit')
    }

    def enter_user_name(self):
        self.user_name_input.set_text(self.user_name)

    def enter_password(self):
        self.password_input.set_text(self.password)

    def click_login(self):
        self.login_btn.click()
