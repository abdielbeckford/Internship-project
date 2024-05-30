Feature: Contact Us page tests

  Scenario: User can open and verify Contact Us page
    Given Open the main page
    When Log in to the page
    And Click on settings option
    And Click on Contact us option
    Then Verify the right page opens
    Then Verify there are at least 4 social media icons