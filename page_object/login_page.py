from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dataclasses import dataclass


@dataclass
class LoginPage():
    driver: WebDriver

    def enter_email(self, email: str):
        email_field = self.get_email_field()
        email_field.send_keys(email)
        self.get_next_button().click()

        """ Without this wait, some tests sometimes fail."""
        wait = WebDriverWait(self.driver, 10)
        wait.until_not(EC.visibility_of_element_located((By.ID, 'identifierId')))

    def get_email_field(self) -> WebElement:
        email_field = self.driver.find_element(By.ID, 'identifierId')
        return email_field

    def get_next_button(self) -> WebElement:
        button = self.driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
        return button

    def enter_password(self, password: str):
        password_field = self.get_password_field()
        password_field.send_keys(password)
        self.get_pw_next_button().click()

    def get_password_field(self) -> WebElement:
        field = self.driver.find_element(By.NAME, 'Passwd')
        return field

    def get_pw_next_button(self) -> WebElement:
        button = self.driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
        return button

    def account_is_present(self) -> bool:
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'gb_mf')))
        search_image = self.driver.find_element(By.CLASS_NAME, 'gb_mf')
        return True

    def alert_password_incorrect(self) -> str:
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'uSvLId')))
        return alert.text

    def alert_email_incorrect(self) -> str:
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.visibility_of_element_located((By.ID, 'next')))
        return alert.text

    def link_forgot_password(self) -> str:
        link = self.driver.find_element(By.ID, 'forgotPassword')
        link.click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, 'smsButton')))
        alert = self.driver.find_element(By.ID, 'smsButton')
        return alert.text

    def link_forgot_email(self) -> str:
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[type="button"]')))
        link = self.driver.find_element(By.CSS_SELECTOR, '[type="button"]')
        link.click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, 'headingSubtext')))
        alert = self.driver.find_element(By.ID, 'headingSubtext')
        return alert.text
