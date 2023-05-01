Feature: Form Submit
    As a new user
    I want to be able to submit a form on the website

    Scenario: User fills out info and submits successfully
        Given the user is on the form page
        When the user enters their name and email
        And clicks on the submit button
        Then the user should be given a confirmation alert

    Scenario: User does not fill out their name therefore failing to submit
        Given the user is on the form page
        When the user enters their email but leaves the name field blank
        And clicks on the submit button
        Then an error message should appear stating that the name field is required

    Scenario: User does not fill out their email therefore failing to submit
        Given the user is on the form page
        When the user enters their name but leaves the email field blank
        And clicks on the submit button
        Then an error message should appear stating that the email field is required

    Scenario: User does not fill out their name or email therefore failing to submit
        Given the user is on the form page
        When the user does not enter their email and name
        And clicks on the submit button
        Then an error message should appear stating that the name field and email field is required