from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from SkypeService import SkypeService
import requests
import shutil
import traceback
import os
from Constants import Settings, SeleniumXpaths, SystemPaths, WebsiteLink, LoadingState
from Credentials import Credentials
 
class DiawiService():
    driver = None
    def __init__(self) -> None:
        chrome_options = Options()
        chrome_options.add_argument(Settings.HEADLESSMODE)
        chrome_options.add_argument(Settings.LOG_LEVEL3)
        chrome_options.add_argument(Settings.IGNORE_CERTIFICATE_ERRORS)
        self.driver = webdriver.Chrome(options=chrome_options)

    def UploadToDiawi(self, full_name, app_path=None, message='', skypeService:SkypeService=None):
        if Credentials.HasDiawiAccount:
            self.driver.get(WebsiteLink.Diawi)

            WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, SeleniumXpaths.LoginPageButton)))
            self.driver.find_element(By.XPATH, SeleniumXpaths.LoginPageButton).click()

            WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, SeleniumXpaths.EmailAddress)))
            self.driver.find_element(By.XPATH, SeleniumXpaths.EmailAddress).send_keys(Credentials.DiawiEmail)

            WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, SeleniumXpaths.Password)))
            self.driver.find_element(By.XPATH, SeleniumXpaths.Password).send_keys(Credentials.DiawiPassword)

            WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, SeleniumXpaths.LoginButton)))
            self.driver.find_element(By.XPATH, SeleniumXpaths.LoginButton).click()

        self.driver.get(WebsiteLink.Diawi)

        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, SeleniumXpaths.FileUploadXpath)))
        self.driver.find_element(By.XPATH, SeleniumXpaths.FileUploadXpath).send_keys(app_path)

        #waiting for loading
        while self.driver.find_element(By.XPATH, SeleniumXpaths.LoadingText).text != LoadingState.Completed:
            continue

        self.driver.find_element(By.XPATH, SeleniumXpaths.SubmitButtonXpath).click()

        WebDriverWait(driver=self.driver, timeout=500).until(EC.presence_of_element_located(((By.XPATH, SeleniumXpaths.UrlLinkElement))))
        link = self.driver.find_element(By.XPATH, SeleniumXpaths.UrlLinkElement).text
        image = self.driver.find_element(By.XPATH, SeleniumXpaths.ImageElementXpath)

        print("Apk Uploaded: ")

        src = ''
        while src == '':
            src = image.get_attribute('src')
            url = src

        response = requests.get(url, stream=True)

        with open(SystemPaths.ImageFolderPath, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

        print("Image Path: ------>")

        try:
            print("Sending message to skype")
            skypeService.SendMsgToSkype(full_name, SystemPaths.ImageFolderPath, f"{message} Diawi Link: {link}", image=True)
            os.remove(SystemPaths.ImageFolderPath)

        except:
            print("An exception occurred")
            traceback.print_exc()
