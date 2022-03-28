import os
from colorama import init, Fore, Style

# Selenium module imports: pip install selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException as TE
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
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


class CodeGenerate:

    def __init__(self)-> None:
        self.driver = self.webdriver()  # Start new webdriver.
  

    def webdriver(self):
        """Start webdriver and return state of it."""
        options = webdriver.ChromeOptions()  # Configure options for Chrome.
        # options.add_extension(self.extension_path)  # Add extension.
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
        # options.add_argument('--user-data-dir=./profiles/')
        # options.add_argument("--user-data-dir=./chrome_profiles/")
        # options.add_argument(f"--profile-directory={profile_dir}")
        driver = webdriver.Chrome(options=options)
        # driver.maximize_window()  # Maximize window to reach all elements.
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

    def demonstration(self) -> None:
        self.window_handles(1)
        self.driver.close()
        self.window_handles(0)
        self.driver.get('chrome-extension://ailoabdmgclmfmhdagmlohpjlbpffblp/index.html')
        time.sleep(3)
        button = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/section/div[2]/button')
        button.click()
        time.sleep(3)
        c = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/section/div/div/div[2]/div[2]')
        code = ''
        for i in self.driver.find_elements(By.XPATH,'//*[@id="root"]/div/div[2]/section/div/div/div[2]/div[2]'):
            code +=str(i.text)

        self.driver.find_element(By.XPATH,'.//button[@class="_10cef _3vpot _1e7AR _1E2xr"]').click()
        time.sleep(2)
        login_code = code.replace('\n','').replace('\r','')

        return login_code


def cls() -> None:
    """Clear console function."""
    # Clear console for Windows using 'cls' and Linux & Mac using 'clear'.
    os.system('cls' if os.name == 'nt' else 'clear')

cls()  # Clear console.
getcode = CodeGenerate() 
getcode.demonstration()

