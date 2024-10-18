@test-fixture-1
Feature: Adding test feature
  Background:
    1. I had no feature files
    2. I have one now though
  @test-fixture-2
  Scenario Outline: Adding test scenario

    Given there was no scenario
    And there was no real need to have any
    Then I added one
    When felt I had to

    Examples:
      | new1 | password| full name           | alias   | company | address     | city  | zip code| phone      |
      | .com | Whatfor | Rabarbeata Gibberish| Rabarbea| GerTrans| Hoan Kiem   | Hanoi | 00120   | +84 666    |
      | .net | Modulo  | Kristian Vikernes   | Varg    | Burzum  | Hordaland 51| Bergen| 5003    | +47 265 356|