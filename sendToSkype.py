from skpy import Skype
import sys
from win11toast import toast

def filter_by_full_name(data, full_name):
    filtered_objects = []

    for obj in data:
        if obj['name'].lower() == full_name.lower():
            filtered_objects.append(obj)

    return filtered_objects[0]

def SendMsgToSkype(full_name, path, message, image=False):
    print("Connecting to skype server\n", full_name, path, message)
    sk = Skype("aashir_raza1602@outlook.com", "@@$hir123")
    print("Successfully Connected to Skype Server\n")

    print("Fetching Contacts\n")
    array = []
    for contact in sk.contacts:
        first_name = contact.name.first
        last_name = contact.name.last
        array.append({"id": contact.id, "name": "{} {}".format(first_name, last_name)})

    print("Successfully Fetched Contacts\n")

    contact = filter_by_full_name(array, full_name)

    print("-------> Sending Message to", contact["name"])

    ch = sk.contacts[contact["id"]].chat
    ch.sendFile(open(path, "rb"),name="jabba", image=image)
    ch.sendMsg(message)

    appIcon = path.split("build")[0]+r"src\main\res\mipmap-xxxhdpi\ic_launcher_round.png"
    if(image):
        toast("Jarvis: App Successfully Sent via Skype", "Jarvis has successfully built and sent the app to {} via Skype Succesfully...".format(contact["name"]), icon=appIcon, image=path)
    else:    
        toast("Jarvis: App Successfully Sent via Skype", "Jarvis has successfully built and sent the app to {} via Skype Succesfully...".format(contact["name"]), icon=appIcon)

    print("-------> Message sent successfully" , contact["name"])

    

# ch = sk.contacts["live:.cid.c53dfb0025e178fa"].chat
# msg = ch.sendMsg("Hello. from python script")

if __name__ == "__main__":
    # Example usage
    print("Welcome to JARVIS send File to skype", sys.argv)

    fullName = sys.argv[1]
    path = sys.argv[2]
    message = sys.argv[3]

    # SendMsgToSkype(fullName, path, message)
