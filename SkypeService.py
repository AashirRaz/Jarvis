from skpy import Skype, chat
from reusableFunctions import notification
from Credentials import Credentials
from reusableFunctions import filter_by_full_name
import threading
from toast import toast
import os
from yaspin import yaspin
from yaspin.spinners import Spinners



class SkypeService:
    def __init__(self) -> None:
        sp1 = startToast("Connecting to Skype Server...")
        global sk
        sk = Skype(Credentials.SkypeUserName, Credentials.SkypePassword)
        stopToast(sp1, "Successfully! Connected to Skype Server")

        sp2 = startToast("Fetching Contacts...")

        self.chats = {}

        for i in range(5):
            self.chats.update(sk.chats.recent())
            
        self.conversations = {}

        stopToast(sp2, "Successfully! Fetched Contacts")

    def SendMsgToSkype(self, full_name, path, message):
        contacts = filter_by_full_name(self.getContacts(), full_name)

        threads = []
        for contact in contacts:
            thread = threading.Thread(target=self.sendMessagesInParallel, args=(contact, path, message))
            thread.start()
            threads.append(thread)

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

    def sendMessagesInParallel(self, contact, path, message, image=False):
        extension = path.split(".")[1]
        contactId = list(self.conversations.keys())[list(self.conversations.values()).index(contact)]
        ch:chat.SkypeChat = sk.chats.chat(contactId)
        ch.sendFile(open(path, "rb"),name=f"{message}.{extension}", image=image)
        ch.sendMsg(message)


    def getContacts(self):
        for i in self.chats.values():
            if type(i) == chat.SkypeSingleChat and bool(i.user and i.user.name and i.user.name.first):
                 self.conversations[i.id] = i.user.name.first + " " + (i.user.name.last if i.user.name.last else "") 
            elif type(i) == chat.SkypeGroupChat and bool(i.topic):
                 self.conversations[i.id] = i.topic

        return self.conversations.values()
    

def startToast(message: str):
    sp = yaspin(text=message, color="cyan")
    sp.start()
    sp.spinner = Spinners.aesthetic

    return sp

def stopToast(sp, message: str):
    sp.text = message
    sp.green.ok("✔")
    