Feature: Login Page
    As a registered user
    I want to fill out the login form to access the platform

    Background:
        Given I am on the Login page

    Scenario: Successful login
        When the user enters the username "Admin"
        And the user enters the password "admin123"
        And the user clicks on the "Login" button
        Then the system should redirect to the "Dashboard" page
        And the Dashboard page header should display the text "Dashboard"

    Scenario: Unsuccessful login
        When the user enters the username "123456789"
        And the user enters the password "123456789"
        And the user clicks on the "Login" button
        Then the system should display an error message "Invalid credentials"
        And the username and password fields should remain visible

    Scenario: Login attempt with empty fields
        When the user leaves the username field empty
        And the user leaves the password field empty
        And the user clicks on the "Login" button
        Then the system should display a "Required" message on both fields
        And the user should remain on the login page