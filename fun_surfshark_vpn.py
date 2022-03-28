import time

import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from driver import wdriver


driver = wdriver()
def generate_code(driver):
    try:
        time.sleep(3)
        driver.execute_script("window.open('about:blank', 'tab2');")
        time.sleep(2)
        driver.switch_to.window('tab2')
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
        # driver.quit()
        print(login_code)
        return login_code

    except Exception as e:
        return "Something Went Wrong."

    finally:
        driver.quit()

generate_code(driver)