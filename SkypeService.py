from skpy import Skype, chat
from reusableFunctions import notification
from Constants import  PathConstants
from Credentials import Credentials
from reusableFunctions import filter_by_full_name
import threading


class SkypeService:
    def __init__(self) -> None:
        print("Connecting to skype server\n")
        global sk
        sk = Skype(Credentials.SkypeUserName, Credentials.SkypePassword)
        print("Successfully Connected to Skype Server\n")
        print("Fetching Contacts\n")    

        self.chats = {}

        for i in range(3):
            self.chats.update(sk.chats.recent())
            
        self.conversations = {}

    def SendMsgToSkype(self, full_name, path, message, image=False):
        contacts = filter_by_full_name(self.getContacts(), full_name)

        for contact in self.getContacts():
            threading.Thread(target=self.sendMessagesInParallel, args=(contact, path, message, image)).start()

        appIcon = path.split("build")[0]+PathConstants.IconPath
        notification("Jarvis: App Successfully Sent via Skype", f"Jarvis has successfully built and sent the app to {[contact['name'] for contact in contacts]} via Skype Succesfully...", appIcon, path)

    def sendMessagesInParallel(self, contact, path, message, image=False):
        extension = path.split(".")[1]
        contactId = list(self.conversations.keys())[list(self.conversations.values()).index(contact)]
        print(contactId)
        ch = sk.chats.chat(contactId)
        ch.sendFile(open(path, "rb"),name=f"{message}.{extension}", image=image)
        ch.sendMsg(message)


    def getContacts(self):
        for i in self.chats.values():
            if type(i) == chat.SkypeSingleChat and bool(i.user and i.user.name and i.user.name.first):
                 self.conversations[i.id] = i.user.name.first + " " + (i.user.name.last if i.user.name.last else "") 
            elif type(i) == chat.SkypeGroupChat and bool(i.topic):
                 self.conversations[i.id] = i.topic

        return self.conversations.values()