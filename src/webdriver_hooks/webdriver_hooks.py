from selenium import webdriver
class WebDriverHooks:

    def __init__(self, driver):
        self.driver = driver

    def set_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def tear_down(self):
        if self.driver:
            self.driver.quit()

    def get_driver(self):
        return self.driver



