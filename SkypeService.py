from skpy import Skype, chat
from Credentials import Credentials
from reusableFunctions import filter_by_full_name
import threading
from toast import toast

class SkypeService:
    def __init__(self) -> None:
        toast("[1/10]", " Connecting to Skype Server...")
        global sk
        sk = Skype(Credentials.SkypeUserName, Credentials.SkypePassword)       
        toast("[2/10]", " Connected to Skype Server Successfully...")
        toast("[3/10]", " Fetching Contacts...")
        self.chats = {}

        for i in range(5):
            self.chats.update(sk.chats.recent())
            
        self.conversations = {}

        toast("[4/10]", " Contacts Fetched Successfully...\n")


    def SendMsgToSkype(self, send_to_whom, message):
        contacts = filter_by_full_name(self.getContacts(), send_to_whom)

        threads = []
        for contact in contacts:
            thread = threading.Thread(target=self.sendMessagesInParallel, args=(contact, message))
            thread.start()
            threads.append(thread)

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

    def sendMessagesInParallel(self, contact, message):
        contactId = list(self.conversations.keys())[list(self.conversations.values()).index(contact)]
        ch:chat.SkypeChat = sk.chats.chat(contactId)
        ch.sendMsg(message)


    def getContacts(self):
        for i in self.chats.values():
            if type(i) == chat.SkypeSingleChat and bool(i.user and i.user.name and i.user.name.first):
                 self.conversations[i.id] = i.user.name.first + " " + (i.user.name.last if i.user.name.last else "") 
            elif type(i) == chat.SkypeGroupChat and bool(i.topic):
                 self.conversations[i.id] = i.topic

        return self.conversations.values()