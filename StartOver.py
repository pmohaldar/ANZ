from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import time
from behave import given, when, then

@given("Launch the browser with the base url")
def step_give(context):
    context.helperfunc.open('https://www.anz.com.au/personal/home-loans/calculators-tools/much-borrow/')
    context.helperfunc.maximize()





@when("Startover button will be displayed if any one field is filled with value ,click on the start over button")
def step_when(context):
    context.helperfunc.find_by_id('expenses').send_keys(1)
    context.helperfunc.find_by_id('addbutton').click()
    context.helperfunc.find_by_id('btnBorrowCalculater').click()
    context.helperfunc.find_by_id('start-over').click()



@then("Form should be refresed")
def step_then(context):
    context.helperfunc.open("https://www.anz.com.au/personal/home-loans/calculators-tools/much-borrow/")

