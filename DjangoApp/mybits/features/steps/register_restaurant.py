from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@given('there is a registered user with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    from django.contrib.auth.models import User
    user = User.objects.create_user(username=username, password=password)
    context.user = user  # Almacenar el usuario en el contexto
    return user

@given('I am on the login page')
def step_given_i_am_on_the_login_page(context):
    context.browser = webdriver.Chrome()
    login_url = 'http://localhost:8000/login/?next=/'
    context.browser.get(login_url)

@when('I enter my username "{username}" and password "{password}" and click the login button')
def step_when_i_enter_username_and_password(context, username, password):
    wait = WebDriverWait(context.browser, 10)  # Espera hasta 10 segundos
    username_input = wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
    username_input.send_keys(username)
    password_input = wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
    password_input.send_keys(password)
    login_button = context.browser.find_element(By.XPATH, '//input[@value="Login"]')
    login_button.click()

@then('I should be on the home page')
def step_then_i_should_be_on_the_home_page(context):
    expected_title = "My Bits Project Home Page"
    actual_title = context.browser.title
    assert expected_title == actual_title, f"Expected title: {expected_title}, Actual title: {actual_title}"

@then('I click the "Booking Restaurant" link in the navbar')
def step_then_i_click_booking_link(context):
    wait = WebDriverWait(context.browser, 10)
    booking_link = wait.until(EC.visibility_of_element_located((By.ID, 'booking-button')))
    booking_link = context.browser.find_element(By.ID, 'booking-button')
    context.browser.execute_script("arguments[0].click();", booking_link)

# @then('I select "{date}" from the date dropdown')
# def step_then_i_select_date(context, date):
#     date_dropdown = Select(context.driver.find_element_by_id('date-dropdown'))
#     date_dropdown.select_by_visible_text(date)

# @then('I select "{time}" from the time dropdown')
# def step_then_i_select_time(context, time):
#     time_dropdown = Select(context.driver.find_element_by_id('time-dropdown'))
#     time_dropdown.select_by_visible_text(time)

# @then('I fill out the booking form with the following details:')
# def step_then_i_fill_out_booking_form(context):
#     table = context.table
#     guests_input = context.driver.find_element_by_id('guests-input')
#     guests_input.send_keys(table[0]['Guests'])

# @then('I select "{restaurant}" from the restaurant dropdown')
# def step_then_i_select_restaurant(context, restaurant):
#     restaurant_dropdown = Select(context.driver.find_element_by_id('restaurant-dropdown'))
#     restaurant_dropdown.select_by_visible_text(restaurant)

# @then('I click the "Create" button')
# def step_then_i_click_create_button(context):
#     create_button = context.driver.find_element_by_id('create-button')
#     create_button.click()

# @then('I should see the booking page')
# def step_then_i_should_see_booking_page(context):
#     assert 'Booking Confirmation' in context.driver.title

# @then('I should see the following details:')
# def step_then_i_should_see_details(context):
#     table = context.table
#     booking_details = WebDriverWait(context.driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'booking-details'))
#     )
#     booking_info = booking_details.text
#     for row in table:
#         for heading, value in row.items():
#             assert value in booking_info

# @then('I close the browser')
# def step_then_i_close_browser(context):
#     context.driver.quit()
