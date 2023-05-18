from splinter.browser import Browser
from selenium import webdriver


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()

def after_scenario(context, scenario):
    context.driver.quit()

def before_all(context):
    context.browser = Browser('chrome', headless=False)

def after_all(context):
    context.browser.quit()
    context.browser = None