@log_in_1
Feature: Login functionality

  Scenario Outline: Unsuccessful login
    Given I am on the YouTube main page
    And I click on Sign In
    When I enter <invalid_email> and click Next
    Then I verify if an error message containing <error_message> is displayed

    Examples:
      | invalid_email      | error_message       |
      | invalid.email@.com | Enter a valid email |

  Scenario: Successful login
    Given I am on the YouTube main page
    And I click on Sign In and select my account
    When I enter a valid email
    And I click Next
    Then I enter a valid password
    And I click Next
    Then I verify that I am successfully logged in
    And I log out
    Then I close the browser

