import time
from SkypeService import SkypeService
import requests
from Constants import  DiawiUrls
from Credentials import Credentials
from toast import toast
import time
 
def UploadToDiawi(send_to_whom, app_path=None, message='', skypeService:SkypeService=None):
        toast("[7/10]", "Uploading to Diawi...")

        job_id = upload_file_to_diawi(app_path)

        diawiLink = ''

        while True:
            status_response = check_upload_status(job_id) #{ "status": number, "message": string "hash"?: string, "link"?: string, "qrcode"?: string }

            status = status_response['status']

            if status == 2000:  # Completed
                print('Upload completed.')
                diawiLink = status_response['link']
                toast("[8/10]", "Successfully Uploaded to Diawi", 'success')
                break
            elif status == 4000:  # Error
                break
            else:
                time.sleep(5)  # Wait before checking again


        if diawiLink:
            toast("[9/10]", "Sending Message to Skype...")
            skypeService.SendMsgToSkype(send_to_whom, f"{message} Diawi Link: {diawiLink}")
            toast("[10/10]", "Successfully Sent Message to Skype", 'success')
        else:
            toast("[9/10]", "Failed to send message to Skype", 'error')

def upload_file_to_diawi(file_path) -> dict[str, str]:
    files = {'file': open(file_path, 'rb')}
    data = {
        'token': Credentials.DiawiApiKey,
        "find_by_udid": 0,
        "installation_notifications": 1,
        "wall_of_apps": 1,
        "callback_emails": "syed.aashir@koderlabs.com,faiq.mahmood@koderlabs.com,qamber.ali@koderlabs.com"
    }

    response = requests.post(DiawiUrls.DIAWI_UPLOAD_URL, files=files, data=data)
    if response.status_code == 200:
        response_data = response.json()
        job_id = response_data['job']
        return job_id
    else:
        raise Exception('Failed to upload file: ' + response.text)

def check_upload_status(job_id) -> dict[str, str]:
    params = {'token': Credentials.DiawiApiKey, 'job': job_id}
    response = requests.get(DiawiUrls.DIAWI_CHECK_STATUS_URL, params=params) 
    if response.status_code == 200:
        response_data = response.json()
        return response_data
    else:
        raise Exception('Failed to check status: ' + response.text)