Feature: Search Gap T-shirts on Next website

  As a user
  I want to search for Gap T-shirts on the Next website
  So that I can buy them online

  Background:
    Given I am on the Next website

@test
  Scenario Outline: Select a specific Gap T-shirt
    Given I have searched for "<product>"
    When I click on a specific "<product>" from the search results
    Then I should see the details of the selected "<product>"

  Examples:
    | product    |
    | Gap T-shirt|
    | Gap Hoodie |
