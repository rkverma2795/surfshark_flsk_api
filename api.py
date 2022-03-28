from flask import Flask, request
# from flask_restful import Resource, Api, reqparse
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
from driver import wdriver
from fun_surfshark_vpn import generate_code

app = Flask(__name__)

driver = wdriver()

@app.route('/login/<string:code>')
def login(code):
    # try:
    time.sleep(5)
    #surfshark login credential
    surfshark_email = "admin@noborders.net"
    surfshark_password = "Surviraladmin789"
    driver.get('https://my.surfshark.com/auth/login')
    time.sleep(randint(1,5))
    driver.find_element_by_name('emailField').send_keys(surfshark_email)
    time.sleep(randint(1,5))
    driver.find_element_by_name('passwordField').send_keys(surfshark_password)
    time.sleep(randint(5,10))
    time.sleep(3)
    button = driver.find_element(By.XPATH,'//*[@id="loginSubmit"]')
    button.click()
    time.sleep(10)
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
    # close_button = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div[5]/a').click()
    driver.quit()
    return "Succesfully logged in"
    # except Exception as e:
    #     return "Something Went Wrong."
    # finally:
    #     driver.close()

if __name__ == '__main__':
    app.run(debug=True)