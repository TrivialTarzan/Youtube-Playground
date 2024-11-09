from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WebDriverHooks:

    def __init__(self):
        self.driver = None

    def set_driver(self):
        # initializing a webdriver

        chrome_options = Options()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled") # -> Prevents bot detection
        chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://allegro.com.allegrosandbox.pl/log-in")
        self.driver.execute_script(
            "document.querySelectorAll('allegro.gdpr.consents').forEach(el => el.remove());"
        )
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tear_down(self):
        if self.driver:
            self.driver.quit()

    def get_driver(self):
        # returns a driver only if initialized (not None)

        if self.driver:
            return self.driver



