from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
path = os.getcwd()+"/drivers/geckodriver"

browser = webdriver.Chrome(desired_capabilities=cap,executable_path=path)
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--disable-dev-shm-using")
chrome_options.add_argument('--disable-gpu')
browser.get('https://birmilyonmarka.com', options = chrome_options)
print(browser.title)
