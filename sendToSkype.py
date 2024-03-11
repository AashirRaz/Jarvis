from skpy import Skype
from reusableFunctions import notification
from Constants import  PathConstants
from Credentials import Credentials
from reusableFunctions import filter_by_full_name
import threading

def init_skype():
    print("Connecting to skype server\n")
    global sk
    sk = Skype(Credentials.SkypeUserName, Credentials.SkypePassword)
    print("Successfully Connected to Skype Server\n")
    print("Fetching Contacts\n")

    global array
    array = []
    for contact in sk.contacts:
            first_name = contact.name.first
            last_name = contact.name.last
            array.append({"id": contact.id, "name": "{} {}".format(first_name, last_name)})



def SendMsgToSkype(full_name, path, message, image=False):

    contacts = filter_by_full_name(array, full_name)

    for contact in contacts:
        threading.Thread(target=sendMessagesInParallel, args=(contact, path, message, image)).start()

    appIcon = path.split("build")[0]+PathConstants.IconPath
    
    notification("Jarvis: App Successfully Sent via Skype", f"Jarvis has successfully built and sent the app to {[contact['name'] for contact in contacts]} via Skype Succesfully...", appIcon, path)

def sendMessagesInParallel(contact, path, message, image=False):
    extension = path.split(".")[1]
    ch = sk.contacts[contact["id"]].chat
    ch.sendFile(open(path, "rb"),name=f"{message}.{extension}", image=image)
    ch.sendMsg(message)