@log_in_1
Feature: log in

  Scenario: Successful login
    Given you are on the Allegro login page
    And you enter your username and password
    Then you click log in
    Then you log out
