from pytest_bdd import scenarios, given, when, then
from pages import NextHomePage

scenarios('../feature/search.feature')

@given('I am on the Next website')
def go_to_next_website(browser):
    NextHomePage(browser).load()

@given('I have searched for "<product>"')
def search_product(browser, product):
    NextHomePage(browser).search_product(product)

@when('I click on a specific "<product>" from the search results')
def select_product(browser, product):
    SearchResultsPage(browser).select_product(product)

@then('I should see the details of the selected "<product>"')
def verify_product_details(browser, product):
    ProductDetailsPage(browser).verify_product_details(product)