import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from page_object.login_page import LoginPage
from webdriver_factory import WebDriverFactory


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        self.email = 'john.smith.junior.junior@gmail.com'
        self.email_incorrect = 'john.smith@gmail.com'
        self.password = 'john1234smith'
        self.password_incorrect = 'john12345smith'

    def setUp(self) -> None:
        self.driver = WebDriverFactory.get_driver()
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://mail.google.com')
        self.login_page = LoginPage(self.driver)
        self.login_page.wait_for_page_is_loaded()
        self.login_page.set_english_local()

    def tearDown(self) -> None:
        self.driver.save_screenshot('test-reports/' + self.id() + '.png')
        self.driver.close()

    def test_valid_values(self):
        """ valid email and valid password """
        """
        self.login_page.enter_email(self.email)
        self.login_page.next_button_click()
        self.login_page.enter_password(self.password)
        self.login_page.password_next_button_click()
        self.assertTrue(self.login_page.wait_for_account_is_present())"""

    def test_valid_email_and_incorrect_password(self):
        """ valid email and incorrect password """
        """
        self.login_page.enter_email(self.email)
        self.login_page.next_button_click()
        self.login_page.enter_password(self.password_incorrect)
        self.login_page.password_next_button_click()
        alert = self.login_page.alert_password_incorrect()
        self.assertIn('Wrong password.', alert)"""

    def test_incorrect_email(self):
        """ incorrect email """
        """
        self.login_page.enter_email(self.email_incorrect)
        self.login_page.next_button_click()
        alert = self.login_page.alert_email_incorrect()
        self.assertEqual('Try again', alert)"""

    def test_forgot_password(self):
        """ Verify the ‘Forgot Password’ functionality """
        """
        self.login_page.enter_email(self.email)
        self.login_page.next_button_click()
        self.login_page.link_forgot_password_click()
        alert = self.login_page.get_alert_sms()
        self.assertEqual('SMS', alert)"""

    def test_forgot_email(self):
        """ Verify the ‘Forgot Email’ functionality """
        """
        self.login_page.link_forgot_email_click()
        alert = self.login_page.get_alert_number_of_phone()
        self.assertEqual('Enter your phone number or recovery email', alert)"""

    ''' 
    I have implemented the basic test cases, imho :). 
    There are many more cases. For example, 
    
    - Verify that there is limit on the total number of unsuccessful attempts
    - Use the tab to navigate from username textbox to password textbox and then to the login button.
    - Verify the login page and all its controls in different browsers
    - Verify the login page by pressing ‘Back button’ of the browser.
      It should not allow you to enter into the system once you log out.
    '''
