Feature: Login to Next Website
    As a user
    I want to login to the Next website
    So that I can access my account
    @test
    Scenario Outline: Successful login with valid credentials
        Given I am on the Next website
        When I enter "<username>" and "<password>"
        And I click on the login button
        # Then I should be logged in successfully

        Examples:
            | username | password |
            | user1    | pass123  |
            # | user2    | pass456  |

    # Scenario: Login with incorrect username
    #     Given I am on the Next website
    #     When I enter "invalid_username" and "pass123"
    #     And I click on the login button
    #     Then I should see an error message

    # Scenario: Login with incorrect password
    #     Given I am on the Next website
    #     When I enter "user1" and "invalid_password"
    #     And I click on the login button
    #     Then I should see an error message

    # Scenario: Login with empty username and password
    #     Given I am on the Next website
    #     When I enter "" and ""
    #     And I click on the login button
    #     Then I should see an error message