import os
from colorama import init, Fore, Style

# Selenium module imports: pip install selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException as TE
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth
# Python default import.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
import json
import time
from random import randint
import random
# from mailtm import Email
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import random
import threading, queue
import pyperclip
from fun_surfshark_vpn import generate_code

with open('cred.txt', 'r') as f:
    for line in f.readlines():
        user_v, pass_v = line.split(' ')

class Login:

    """Main class of the hCaptcha solver."""
    def __init__(self)-> None:
        # self.extension_path = './Tampermonkey.crx'
        self.driver = self.webdriver()  # Start new webdriver.
  
    def webdriver(self):
        """Start webdriver and return state of it."""
        options = webdriver.ChromeOptions()  # Configure options for Chrome.
        # options.add_extension()  # Add extension.
        options.add_argument('--lang=en')  # Set webdriver language to English.
        options.add_argument('log-level=3')  # No logs is printed.
        options.add_argument('--mute-audio')  # Audio is muted.
        options.add_argument("--enable-webgl-draft-extensions")
        options.add_argument("--ignore-gpu-blocklist")
        # options.add_argument("--user-data-dir=./chromeprofile/profiles/" + str(user_v))
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


    def element_clickable(self, element: str) -> None:
        """Click on element if it's clickable using Selenium."""
        WDW(self.driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, element))).click()


    def element_visible(self, element: str):
        """Check if element is visible using Selenium."""
        return WDW(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, element)))


    def window_handles(self, window_number: int) -> None:
        """Check for window handles and wait until a specific tab is opened."""
        WDW(self.driver, 30).until(lambda _: len(
            self.driver.window_handles) == window_number + 1)
        # Switch to asked tab.
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    def code_verfication(self) -> None:
        code = generate_code(self.driver)
        time.sleep(15)
        # self.window_handles(1)
        # self.driver.close()
        # self.window_handles(0)
        #surfshark login credential
        surfshark_email = "admin@noborders.net"
        surfshark_password = "Surviraladmin789"

        self.driver.get('https://my.surfshark.com/auth/login')
        time.sleep(randint(1,5))
        self.driver.find_element_by_name('emailField').send_keys(surfshark_email)
        time.sleep(randint(1,5))
        self.driver.find_element_by_name('passwordField').send_keys(surfshark_password)
        time.sleep(randint(5,10))
        time.sleep(3)
        button = self.driver.find_element(By.XPATH,'//*[@id="loginSubmit"]')
        button.click()
        time.sleep(10)
        profile = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[2]/div[1]/div[2]/button')
        profile.click()
        time.sleep(3)
        login_with_code = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/a[1]/div/div[2]/div')
        login_with_code.click()
        time.sleep(5)
        login_code =self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div/div[2]/div[2]/div/div/form/div[4]/div/span[1]/input')
        time.sleep(2)
        login_code.click()
        login_code.send_keys(code)
        login = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[2]/div[2]/div/div/form/div[5]/button')
        login.click()
        time.sleep(5)
        close_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div[5]/a').click()
        

def cls() -> None:
    """Clear console function."""
    # Clear console for Windows using 'cls' and Linux & Mac using 'clear'.
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    cls()  # Clear console.
    time.sleep(10)
    loginwithcode = Login() 
    loginwithcode.code_verfication()  
