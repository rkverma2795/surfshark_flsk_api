from flask import Flask
import requests
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

# from fun_surfshark_vpn import generate_code


app = Flask(__name__)


with open('cred.txt', 'r') as f:
    for line in f.readlines():
        user_v, pass_v = line.split(' ')


def wdriver():
    """Start webdriver and return state of it."""
    options = webdriver.ChromeOptions()  # Configure options for Chrome.
    options.add_argument('--lang=en')  # Set webdriver language to English.
    options.add_argument('log-level=3')  # No logs is printed.
    options.add_argument('--mute-audio')  # Audio is muted.
    options.add_argument("--enable-webgl-draft-extensions")
    options.add_argument("--ignore-gpu-blocklist")
    options.add_extension("./surfshark.crx")#crx file path
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

    options.add_experimental_option("prefs", prefs)
    options.add_argument("--user-data-dir=./chromeprofile/profiles/" + user_v)
    prefs = {"credentials_enable_service": True,
             "profile.password_manager_enabled": True}
    options.add_experimental_option("prefs", prefs)
    # service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome( options=options)
    # driver = webdriver.Chrome(service=service, options=options)
    return driver

driver = wdriver()

def element_clickable(element: str) -> None:
    """Click on element if it's clickable using Selenium."""
    WDW(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, element))).click()


def element_visible( element: str):
    """Check if element is visible using Selenium."""
    return WDW(driver, 20).until(EC.visibility_of_element_located(
        (By.XPATH, element)))


def window_handles(window_number: int) -> None:
    """Check for window handles and wait until a specific tab is opened."""
    WDW(driver, 30).until(lambda _: len(
        driver.window_handles) == window_number + 1)
    # Switch to asked tab.
    driver.switch_to.window(driver.window_handles[window_number])


def generate_code(driver):
    time.sleep(3)
    driver.get('chrome-extension://ailoabdmgclmfmhdagmlohpjlbpffblp/index.html')
    time.sleep(2)
    button = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/section/div[2]/button')
    button.click()
    time.sleep(3)
    c = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/section/div/div/div[2]/div[2]')
    code = ''
    for i in driver.find_elements(By.XPATH,'//*[@id="root"]/div/div[2]/section/div/div/div[2]/div[2]'):
        code +=str(i.text)

    driver.find_element(By.XPATH,'.//button[@class="_10cef _3vpot _1e7AR _1E2xr"]').click()
    time.sleep(2)
    login_code = code.replace('\n','').replace('\r','')
    print(login_code)

    return login_code

code = generate_code(driver)
print(code)

@app.route('/login-with-code/{code}')
def login():
    time.sleep(15)
    window_handles(1)
    driver.close()
    window_handles(0)
    # #surfshark login credential
    # surfshark_email = "admin@noborders.net"
    # surfshark_password = "Surviraladmin789"

    # driver.get('https://my.surfshark.com/auth/login')
    # time.sleep(randint(1,5))
    # driver.find_element_by_name('emailField').send_keys(surfshark_email)
    # time.sleep(randint(1,5))
    # driver.find_element_by_name('passwordField').send_keys(surfshark_password)
    # time.sleep(randint(5,10))
    # time.sleep(3)
    # button = driver.find_element(By.XPATH,'//*[@id="loginSubmit"]')
    # button.click()
    # time.sleep(10)
    profile = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[2]/div[1]/div[2]/button')
    profile.click()
    login_with_code = driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/a[1]/div/div[2]/div')
    login_with_code.click()
    time.sleep(5)
    login_code = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div/div[2]/div[2]/div/div/form/div[4]/div/span[1]/input')
    time.sleep(2)
    login_code.click()
    login_code.send_keys(code)
    login = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[2]/div[2]/div/div/form/div[5]/button')
    login.click()
    time.sleep(5)
    close_button = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div[5]/a').click()

    return True
    