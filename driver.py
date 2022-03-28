import time
import os
import zipfile
import json
import time
from random import randint
import random
import threading, queue

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException as TE
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium_stealth import stealth

with open('cred.txt', 'r') as f:
    for line in f.readlines():
        user_v, pass_v = line.split(' ')

def getfakename():
    driver = webdriver.Chrome(executable_path='/home/dell/Desktop/surfshark_flask_api/chromedriver')

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://www.fakenamegenerator.com/')
    
    address_ele = WDW(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "address")))
    username = address_ele.find_element_by_tag_name("h3").text
    time.sleep(3)

    driver.quit()
    return username

username = getfakename()
clean_name = str(username).replace(" ","_").replace(".","_")
print(clean_name)
user_profiles = "./surfshark_flask_api/profiles/" + str(clean_name)
if not os.path.exists(user_profiles):
    os.makedirs(user_profiles)

def wdriver():
    """Start webdriver and return state of it."""
    options = webdriver.ChromeOptions()  # Configure options for Chrome.
    # options.add_extension()  # Add extension.
    options.add_argument('--lang=en')  # Set webdriver language to English.
    options.add_argument('log-level=3')  # No logs is printed.
    options.add_argument('--mute-audio')  # Audio is muted.
    options.add_argument("--enable-webgl-draft-extensions")
    options.add_argument("--ignore-gpu-blocklist")
    # options.add_argument("--user-data-dir=./chromeprofile/profiles/" + str(clean_name))
    prefs = {"credentials_enable_service": True,
         "profile.password_manager_enabled": True}
    options.add_experimental_option("prefs", prefs)
    options.add_extension('./surfshark.crx')#crx file path
    options.add_argument('--no-sandbox')
    options.add_argument('--autoplay-policy=no-user-gesture-required')
    options.add_argument('--start-maximized')    
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-blink-features")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--enable-javascript")
    options.add_argument("--disable-notifications")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--enable-popup-blocking")
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("excludeSwitches", [
        "enable-logging",
        "enable-automation",
        "ignore-certificate-errors",
        "safebrowsing-disable-download-protection",
        "safebrowsing-disable-auto-update",
        "disable-client-side-phishing-detection"])
    options.add_argument("disable-infobars")
    driver = webdriver.Chrome(executable_path='./chromedriver', options=options)
    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
    return driver
