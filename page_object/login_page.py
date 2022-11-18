from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dataclasses import dataclass

@dataclass
class LoginPage():
    driver: WebDriver

    def wait_for_page_is_loaded(self) -> None:
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.title_is("Gmail"))

    def set_english_local(self) -> None:
        language_chooser = self.driver.find_element(By.XPATH, '//*[@id="lang-chooser"]/div/div[1]')
        language_chooser.click()
        language_ul = self.driver.find_elements(By.TAG_NAME, 'li')
        index = 0
        for language_li in language_ul:
            if language_li.text == 'English (United States)':
                break
            index += 1
        language_ul[index].click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[type="button"]')))

    def enter_email(self, email: str) -> None:
        email_field = self.get_email_field()
        email_field.send_keys(email)

    def next_button_click(self) -> None:
        self.get_next_button().click()
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

    def password_next_button_click(self) -> None:
        self.get_password_next_button().click()

    def get_password_field(self) -> WebElement:
        field = self.driver.find_element(By.NAME, 'Passwd')
        return field

    def get_password_next_button(self) -> WebElement:
        button = self.driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
        return button

    def wait_for_account_is_present(self) -> bool:
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'loading')))
        return True

    def alert_password_incorrect(self) -> str:
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'uSvLId')))
        return alert.text

    def alert_email_incorrect(self) -> str:
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.visibility_of_element_located((By.ID, 'next')))
        return alert.text

    def link_forgot_password_click(self) -> None:
        link = self.driver.find_element(By.ID, 'forgotPassword')
        link.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, 'smsButton')))

    def get_alert_sms(self) -> str:
        alert = self.driver.find_element(By.ID, 'smsButton')
        return alert.text

    def link_forgot_email_click(self) -> None:
        link = self.driver.find_element(By.CSS_SELECTOR, '[type="button"]')
        link.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, 'headingSubtext')))

    def get_alert_number_of_phone(self) -> str:
        alert = self.driver.find_element(By.ID, 'headingSubtext').text
        return alert
