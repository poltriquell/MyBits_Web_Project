Feature: Login and Booking
  In order to make a restaurant booking
  As a registered user
  I want to log in and fill out the booking form

  Background:
    Given there is a registered user with username "ElQuique" and password "hola12345"

  Scenario: Log in and make a restaurant booking
    Given I am on the login page
    When I enter my username "ElQuique" and password "hola12345" and click the login button
    Then I should be on the home page
    And I click the "Booking Restaurant" link in the navbar
    # And I select "2023-05-23" from the date dropdown
    # And I select "19:00" from the time dropdown
    # And I fill out the booking form with the following details:
    #   | Guests |
    #   | 4      |
    # And I select "Restaurante vegano de Pol Triquel" from the restaurant dropdown
    # And I click the "Create" button
    # Then I should see the booking page
    # And I should see the following details:
    #   | Restaurant                         | Date                 | People Number  | Client         |
    #   | Restaurante vegano de Pol Triquell | May 23, 2023, 7 p.m. |      4         | Don Enric      |