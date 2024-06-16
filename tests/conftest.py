# import pytest
# from selenium import webdriver

# @pytest.fixture
# def browser():
#     # Initialize ChromeDriver
#     driver = webdriver.Chrome()

#     # Make its calls wait up to 10 seconds for elements to appear
#     driver.implicitly_wait(10)

#     # Return the driver object at the end of setup
#     yield driver

#     # For cleanup, quit the driver
#     from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get("https://www.google.com/")
#     driver.quit()

# from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get("https://www.google.com/")