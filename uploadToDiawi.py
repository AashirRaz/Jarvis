from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import requests
import shutil
import traceback
import os
import sendToSkype
from Constants import Settings, SeleniumXpaths, SystemPaths, WebsiteLink, LoadingState
 

def UploadToDiawi(full_name, app_path, message):
    count = 0
    for path in os.listdir(SystemPaths.ImageFolderPath):
        # check if current path is a file
        if os.path.isfile(os.path.join(SystemPaths.ImageFolderPath, path)):
            count += 1

    chrome_options = Options()
    chrome_options.add_argument(Settings.HEADLESSMODE)
    chrome_options.add_argument(Settings.LOG_LEVEL3)
    chrome_options.add_argument(Settings.IGNORE_CERTIFICATE_ERRORS)

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(WebsiteLink.Diawi)

    element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, SeleniumXpaths.FileUploadXpath)))

    fileupload = driver.find_element(By.XPATH, SeleniumXpaths.FileUploadXpath).send_keys(app_path)

    #waiting for loading
    while driver.find_element(By.XPATH, SeleniumXpaths.LoadingText).text != LoadingState.Completed:
        continue

    submitbutton = driver.find_element(By.XPATH, SeleniumXpaths.SubmitButtonXpath).click()

    element = WebDriverWait(driver=driver, timeout=500).until(EC.presence_of_element_located(((By.XPATH, SeleniumXpaths.UrlLinkElement))))

    link = driver.find_element(By.XPATH, SeleniumXpaths.UrlLinkElement).text
    image = driver.find_element(By.XPATH, SeleniumXpaths.ImageElementXpath)
    src = ''
    while src == '':
        src = image.get_attribute('src')
        url = src

    response = requests.get(url, stream=True)

    with open(os.path.join(SystemPaths.ImageFolderPath, f"app_qrcode{count + 1}.png"), 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

    print("image has been downloaded")

    try:
        filePath = os.path.join(SystemPaths.ImageFolderPath, f"app_qrcode{count + 1}.png")
        sendToSkype.SendMsgToSkype(full_name, filePath, f"{message} Diawi Link: {link}", image=True)

    except:
        print("An exception occurred")
        traceback.print_exc()

