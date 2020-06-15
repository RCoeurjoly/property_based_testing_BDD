Feature: Multiply integers

  Scenario: Multiply integers with zero
    Given I have any integer
    When we multiply it by zero
    Then we should get a zero
