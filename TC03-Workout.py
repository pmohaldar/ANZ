from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import time
from behave import given, when, then


@given('Launch the browser with the base url')
def step(context):
    context.helperfunc.open('https://www.anz.com.au/personal/home-loans/calculators-tools/much-borrow/')
    context.helperfunc.maximize()

@when('Living expense field is filled')
def enter_Living(context):
    context.helperfunc.find_by_id('expenses').send_keys("1")

@when('Click on Workout how much I can borrow')
def click_on_workout_button(context):
    context.helperfunc.find_by_id('btnBorrowCalculater').click()


@then("Error message 'Based on the details you've entered, we're unable to give you an estimate of your borrowing power with this calculator. For questions, call us on 1800 035 500.'should be shown")
def see_login_message(context):
    added_item = context.helperfunc.find_by_xpath("//span[@class='borrow__error__text']").text
    print(added_item)



