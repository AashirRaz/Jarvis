from skpy import Skype
from win11toast import toast
from Constants import Skype as SkypeConstants
import threading


def init_skype():
    print("Connecting to skype server\n")
    global sk
    sk = Skype(SkypeConstants.UserName, SkypeConstants.Password)
    print("Successfully Connected to Skype Server\n")
    print("Fetching Contacts\n")

    global array
    array = []
    for contact in sk.contacts:
            first_name = contact.name.first
            last_name = contact.name.last
            array.append({"id": contact.id, "name": "{} {}".format(first_name, last_name)})
    print("Successfully Fetched Contacts\n")



def filter_by_full_name(skypeContacts:list[object], full_names: list[str]) -> list[object]:
    filtered_objects = []
    for contact in skypeContacts:
        for name in full_names:
            if contact["name"].lower() == name.lower():
                filtered_objects.append(contact)

    return filtered_objects

def SendMsgToSkype(full_name, path, message, image=False):

    print("------->", full_name, path , message, image)

    contacts = filter_by_full_name(array, full_name)

    print("-------> Sending Message to", [contact["name"] for contact in contacts])

    for contact in contacts:
        threading.Thread(target=sendMessagesInParallel, args=(contact, path, message, image)).start()

    appIcon = path.split("build")[0]+SkypeConstants.IconPath

    if(image):
        toast("Jarvis: App Successfully Sent via Skype", f"Jarvis has successfully built and sent the app to {[contact['name'] for contact in contacts]} via Skype Succesfully...", icon=appIcon, image=path)
    else:    
        toast("Jarvis: App Successfully Sent via Skype", f"Jarvis has successfully built and sent the app to {[contact['name'] for contact in contacts]} via Skype Succesfully...", icon=appIcon, on_click=path)


def sendMessagesInParallel(contact, path, message, image=False):
    print("=======> Sending Message to", path)
    extension = path.split(".")[1]
    ch = sk.contacts[contact["id"]].chat
    ch.sendFile(open(path, "rb"),name=f"{message}.{extension}", image=image)
    ch.sendMsg(message)



init_skype()
