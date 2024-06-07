import time
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
from toast import toast
 
class DiawiService():
    driver = None
    def __init__(self) -> None:
        chrome_options = Options()
        # chrome_options.add_argument(Settings.HEADLESSMODE)
        chrome_options.add_argument(Settings.LOG_LEVEL3)
        chrome_options.add_argument(Settings.IGNORE_CERTIFICATE_ERRORS)
        self.driver = webdriver.Chrome(options=chrome_options)

    def UploadToDiawi(self, full_name, app_path=None, message='', skypeService:SkypeService=None, name=''):
        toast("[7/10]", "Uploading to Diawi...")
        
        import requests
        import time

        DIAWI_UPLOAD_URL = 'https://upload.diawi.com/'
        DIAWI_CHECK_STATUS_URL = 'https://upload.diawi.com/status'
        API_TOKEN = 'h65ZXIeebgo5bA2kH2cmsm2ShOmf7zad4CAZIlxcoA'

    def upload_file_to_diawi(self, file_path):
        files = {'file': open(file_path, 'rb')}
        data = {
            'token': API_TOKEN,
            'wall_of_apps': 0,
            'comment': 'Uploaded via API'
        }

        response = requests.post(DIAWI_UPLOAD_URL, files=files, data=data)
        if response.status_code == 200:
            response_data = response.json()
            job_id = response_data['job']
            return job_id
        else:
            raise Exception('Failed to upload file: ' + response.text)

    def check_upload_status(self, job_id):
        params = {'token': API_TOKEN, 'job': job_id}
        response = requests.get(DIAWI_CHECK_STATUS_URL, params=params)
        if response.status_code == 200:
            response_data = response.json()
            return response_data
        else:
            raise Exception('Failed to check status: ' + response.text)

    def main():
        file_path = '/Users/aashirraza/Downloads/app-release.apk'  # Replace with your file path

        print('Uploading file to Diawi...')
        job_id = self.upload_file_to_diawi(file_path)
        print(f'Job ID: {job_id}')

        while True:
            status_response = check_upload_status(job_id)
            status = status_response['status']

            if status == 2000:  # Completed
                print('Upload completed.')
                print('Link:', status_response['link'])
                break
            elif status == 4000:  # Error
                print('Upload failed:', status_response['message'])
                break
            else:
                progress = status_response.get('progress', 'Unknown')
                print(f'Upload progress: {progress}%')
                time.sleep(5)  # Wait before checking again


        toast("[8/10]", "Successfully Uploaded to Diawi", 'success')

        toast("[9/10]", "Sending Message to Skype...")
        skypeService.SendMsgToSkype(full_name, SystemPaths.ImageFolderPath, f"{message} Diawi Link: {link}", image=True, name=name)
        os.remove(SystemPaths.ImageFolderPath)
        toast("[10/10]", "Successfully Sent Message to Skype", 'success')

