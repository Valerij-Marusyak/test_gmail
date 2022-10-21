import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from page_object.login_page import LoginPage


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        self.email = 'john.smith.junior.junior@gmail.com'
        self.email_incorrect = 'john.smith@gmail.com'
        self.password = 'john1234smith'
        self.password_incorrect = 'john12345smith'

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://mail.google.com')
        self.login_page = LoginPage(self.driver)

    def tearDown(self) -> None:
        self.driver.save_screenshot("screenshots/" + self.id() + '.png')
        self.driver.close()

    def test_01(self):
        """ valid email and valid password """
        self.login_page.enter_email(self.email)
        self.login_page.enter_password(self.password)
        self.assertTrue(self.login_page.account_is_present())

    def test_02(self):
        """ valid email and incorrect password """
        self.login_page.enter_email(self.email)
        self.login_page.enter_password(self.password_incorrect)
        alert = self.login_page.alert_password_incorrect()
        self.assertIn('Неправильний пароль.', alert)

    def test_03(self):
        """ incorrect email """
        self.login_page.enter_email(self.email_incorrect)
        alert = self.login_page.alert_email_incorrect()
        self.assertEqual('Повторити спробу', alert)

    def test_04(self):
        """ Verify the ‘Forgot Password’ functionality """
        self.login_page.enter_email(self.email)
        alert = self.login_page.link_forgot_password()
        self.assertEqual('SMS', alert)

    def test_05(self):
        """ Verify the ‘Forgot Email’ functionality """
        alert = self.login_page.link_forgot_email()
        self.assertEqual('Введіть номер телефону або резервну електронну адресу', alert)

    ''' 
    I have implemented the basic test cases, imho :). 
    There are many more cases. For example, 
    
    - Verify that there is limit on the total number of unsuccessful attempts
    - Use the tab to navigate from username textbox to password textbox and then to the login button.
    - Verify the login page and all its controls in different browsers
    - Verify the login page by pressing ‘Back button’ of the browser.
      It should not allow you to enter into the system once you log out.
    
    Unfortunately, I did not complete them all, because the time for the test task has already ended. 
    '''
