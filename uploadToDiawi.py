from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import sendToSkype
import requests
import shutil
import traceback
import os
from Constants import Settings, SeleniumXpaths, SystemPaths, WebsiteLink, LoadingState
from Credentials import Credentials
 

def selenium_init():
    chrome_options = Options()
    chrome_options.add_argument(Settings.HEADLESSMODE)
    chrome_options.add_argument(Settings.LOG_LEVEL3)
    chrome_options.add_argument(Settings.IGNORE_CERTIFICATE_ERRORS)

    driver = webdriver.Chrome(options=chrome_options)
    return driver

def UploadToDiawi(full_name, app_path=None, message=''):
    driver = selenium_init()

    driver.get(WebsiteLink.Diawi)

    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, SeleniumXpaths.LoginPageButton)))
    driver.find_element(By.XPATH, SeleniumXpaths.LoginPageButton).click()

    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, SeleniumXpaths.EmailAddress)))
    driver.find_element(By.XPATH, SeleniumXpaths.EmailAddress).send_keys(Credentials.DiawiEmail)

    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, SeleniumXpaths.Password)))
    driver.find_element(By.XPATH, SeleniumXpaths.Password).send_keys(Credentials.DiawiPassword)

    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, SeleniumXpaths.LoginButton)))
    driver.find_element(By.XPATH, SeleniumXpaths.LoginButton).click()

    driver.get(WebsiteLink.Diawi)

    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, SeleniumXpaths.FileUploadXpath)))

    driver.find_element(By.XPATH, SeleniumXpaths.FileUploadXpath).send_keys(app_path)

    #waiting for loading
    while driver.find_element(By.XPATH, SeleniumXpaths.LoadingText).text != LoadingState.Completed:
        continue

    driver.find_element(By.XPATH, SeleniumXpaths.SubmitButtonXpath).click()

    WebDriverWait(driver=driver, timeout=500).until(EC.presence_of_element_located(((By.XPATH, SeleniumXpaths.UrlLinkElement))))

    link = driver.find_element(By.XPATH, SeleniumXpaths.UrlLinkElement).text
    image = driver.find_element(By.XPATH, SeleniumXpaths.ImageElementXpath)

    src = ''
    while src == '':
        src = image.get_attribute('src')
        url = src

    response = requests.get(url, stream=True)

    with open(SystemPaths.ImageFolderPath, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response


    try:
        sendToSkype.SendMsgToSkype(full_name, SystemPaths.ImageFolderPath, f"{message} Diawi Link: {link}", image=True)
        os.remove(SystemPaths.ImageFolderPath)

    except:
        print("An exception occurred")
        traceback.print_exc()
