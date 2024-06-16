from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import rsa

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        self.password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        self.login_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-button"))
        )

    def enter_username(self, username):
        self.username_field.clear()
        self.username_field.send_keys(username)

    def enter_password(self, password):
        self.password_field.clear()
        # Encrypt the password before sending
        encrypted_password = encrypt(password)
        def encrypt(password):
            # Generate RSA key pair
            public_key, private_key = rsa.newkeys(2048)

            # Encrypt the password using the public key
            encrypted_password = rsa.encrypt(password.encode(), public_key)

            return encrypted_password

        # Usage example:

        # encrypted_password = encrypt("my_password")
        # self.password_field.send_keys(encrypted_password)
    def click_login_button(self):
        self.login_button.click()