from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import time
from behave import given, when, then


@given('Once the browser is launched give the url')
def step(context):
    context.helperfunc.open('https://www.anz.com.au/personal/home-loans/calculators-tools/much-borrow/')
    context.helperfunc.maximize()
@when('Fill in all the Value fields for applicant type is single and property is home to buy')
def enter_Living(context):
    context.helperfunc.find_by_id('expenses').send_keys("500")

