Feature: Login functionality on Next website

  Scenario: Successful login with valid credentials
    Given I am on the Next website login page
    When I enter valid username and password
    And I click on the login button
    Then I should be redirected to the user dashboard

  Scenario: Unsuccessful login with invalid credentials
    Given I am on the Next website login page
    When I enter invalid username and password
    And I click on the login button
    Then I should see an error message