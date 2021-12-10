Feature: Normal Employee
  Scenario: Minimum sale of an employee
    Given an employee
    When I set list sales
    Then I get the salary must be greater than or equal to $930