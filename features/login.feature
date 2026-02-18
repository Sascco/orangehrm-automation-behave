Feature: User Authentication

  As a registered user
  I want to log into the platform
  So that I can access my dashboard

  Background:
    Given the user is on the Login page

  Scenario Outline: Login validation
    When the user attempts to log in with username "<username>" and password "<password>"
    Then the system should display "<result>"

  Examples:
    | username   | password   | result              |
    | Admin      | admin123   | Dashboard           |
    | 123456789  | 123456789  | Invalid credentials |
    |            |            | Required fields     |