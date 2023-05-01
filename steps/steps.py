from behave import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('the user is on the form page')
def step_impl(context):
    context.browser.get('http://127.0.0.1:5500/index.html')

@when('the user enters their name and email')
def step_impl(context):
    name_input = context.browser.find_element(By.ID,'name')
    email_input = context.browser.find_element(By.ID,'email')
    name_input.send_keys('John Doe')
    email_input.send_keys('johndoe@example.com')

@when('clicks on the submit button')
def step_impl(context):
    submit_button = WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((By.ID, "submit")))
    context.browser.execute_script("arguments[0].click();", submit_button)

@then('the user should be given a confirmation alert')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    alert = wait.until(EC.alert_is_present())
    alert_text = alert.text
    assert alert_text == 'Form submitted successfully'

@when('the user enters their email but leaves the name field blank')
def step_impl(context):
    name_input = context.browser.find_element(By.ID,'name')
    email_input = context.browser.find_element(By.ID,'email')
    name_input.send_keys('')
    email_input.send_keys('johndoe@example.com')

@then('an error message should appear stating that the name field is required')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    alert = wait.until(EC.alert_is_present())
    alert_text = alert.text
    assert alert_text == 'Name must be filled out'

@when('the user enters their name but leaves the email field blank')
def step_impl(context):
    name_input = context.browser.find_element(By.ID,'name')
    email_input = context.browser.find_element(By.ID,'email')
    name_input.send_keys('John Doe')
    email_input.send_keys('')

@then('an error message should appear stating that the email field is required')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    alert = wait.until(EC.alert_is_present())
    alert_text = alert.text
    assert alert_text == 'Email must be filled out'

@when('the user does not enter their email and name')
def step_impl(context):
    name_input = context.browser.find_element(By.ID,'name')
    email_input = context.browser.find_element(By.ID,'email')
    name_input.send_keys('')
    email_input.send_keys('')

@then('an error message should appear stating that the name field and email field is required')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    alert = wait.until(EC.alert_is_present())
    alert_text = alert.text
    assert alert_text == 'Name and Email must be filled out'

@then('the form should be submitted successfully')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    alert = wait.until(EC.alert_is_present())
    alert_text = alert.text
    assert alert_text == 'Form submitted successfully'
