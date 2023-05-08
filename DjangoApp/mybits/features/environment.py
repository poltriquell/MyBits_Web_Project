from os import system
from selenium import webdriver

chrome_options = webdriver.ChromeOptions() # Configuración de Chrome
chrome_options.add_argument("start-maximized"); # open Browser in maximized mode
chrome_options.add_argument("disable-infobars"); # disabling infobars
chrome_options.add_argument("--disable-extensions"); # disabling extensions
chrome_options.add_argument("--disable-gpu"); # applicable to windows os only
chrome_options.add_argument("--disable-dev-shm-usage"); # overcome limited resource problems
chrome_options.add_argument("--headless")  # Ejecutar Chrome en modo headless para pruebas sin interfaz gráfica
chrome_options.add_argument('--no-sandbox')  # Bypass OS security model

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=chrome_options)
driver.get("https://google.com");

from splinter.browser import Browser

def before_all(context):
    context.browser = Browser('chrome', headless=True)

def after_all(context):
    context.browser.quit()
    context.browser = None