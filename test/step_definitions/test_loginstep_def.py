from pytest_bdd import given, when, then, parsers
from pages import LoginPage
from pytest_bdd import scenarios
import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

scenarios('../../test_resources/features/login.feature')

@given('I am on the Next website')  # Add a function declaration here
def go_to_next_website(driver):
    driver.get("https://www.next.co.uk/")
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//*[@id='platform_modernisation_header']/header/div[1]/nav/div[2]/div[2]/div[2]/div/a/img").click()
    driver.implicitly_wait(10)


# @when(parsers.parse('I enter "{username}" and "{password}"'))  # Add a function declaration here
# def enter_credentials(driver, username, password):
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "EmailOrAccountNumber"))).send_keys(username)
#     username = "jebinjosek@gmail.com"
#     password = "Passwsord@200"
#     driver.find_element(By.ID, "EmailOrAccountNumber").send_keys(username)
#     driver.find_element(By.ID, "Password").send_keys(password)

# @when('I click on the login button')  # Add a function declaration here
# def click_login_button(driver):
#     driver.find_element(By.ID, "SignInNow").click()

# @when('I click on the login button')  # Add a function declaration here
# def click_login_button(driver):
#     LoginPage(driver).click_login_button()



