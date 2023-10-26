from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import requests
import shutil
from skpy import Skype
import traceback
import os
import sendToSkype
 

def UploadToDiawi(full_name, app_path, message):
    imageFolderPath = r"C:\AashirRaza\Scripts\diawiScreenshots"
    fileUploadXpath = "/html/body/section/section[2]/div[1]/form/div[1]/div[2]/input"
    loadingText = "/html/body/section/section[2]/div[1]/form/div[1]/div[1]/div/div/div/ul/li/div[3]"
    submitButtonXpath = "/html/body/section/section[2]/div[1]/form/div[3]/input"
    urlLinkElement = r"/html/body/section/section[2]/div[1]/div/div[1]/div[2]/a"
    imageElementXpath = r'//*[@id="main-container"]/section[2]/div[1]/div/div[2]/img'



    class SeleniumConstants:
        HEADLESSMODE = "--headless"
        LOG_LEVEL3 = "--log-level=3"
        IGNORE_CERTIFICATE_ERRORS = "--ignore-certificate-errors"


    count = 0
    for path in os.listdir(imageFolderPath):
        # check if current path is a file
        if os.path.isfile(os.path.join(imageFolderPath, path)):
            count += 1

    chrome_options = Options()
    chrome_options.add_argument(SeleniumConstants.HEADLESSMODE)
    chrome_options.add_argument(SeleniumConstants.LOG_LEVEL3)
    chrome_options.add_argument(SeleniumConstants.IGNORE_CERTIFICATE_ERRORS)

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.diawi.com/")

    element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, fileUploadXpath)))

    fileupload = driver.find_element(By.XPATH, fileUploadXpath).send_keys(app_path)

    #waiting for loading
    while driver.find_element(By.XPATH, loadingText).text != "100%":
        continue

    submitbutton = driver.find_element(By.XPATH, submitButtonXpath).click()

    element = WebDriverWait(driver=driver, timeout=500).until(EC.presence_of_element_located(((By.XPATH, urlLinkElement))))

    link = driver.find_element(By.XPATH, urlLinkElement).text
    image = driver.find_element(By.XPATH, imageElementXpath)
    src = ''
    while src == '':
        src = image.get_attribute('src')
        url = src

    response = requests.get(url, stream=True)

    with open(os.path.join(imageFolderPath, f"app_qrcode{count + 1}.png"), 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

    print("image has been downloaded")


    try:
        
        filePath = os.path.join(imageFolderPath, f"app_qrcode{count + 1}.png")
        sendToSkype.SendMsgToSkype(full_name, filePath, "{} Diawi Link: {}".format(message, link), image=True)

    except:
        print("An exception occurred")
        traceback.print_exc()

