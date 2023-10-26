from win11toast import toast
import sendToSkype

def SecondNotification(path, message):
    a = toast('Hello', 'Type anything', input='reply', button={'activationType': 'protocol', 'arguments': 'http:', 'content': 'Send To Skype', 'hint-inputId': 'reply'})

    if(a['arguments'] == "http:"):
        sendToSkype.SendMsgToSkype(a['user_input']['reply'], path, message)

def GeneralNotification(path, message):
    toast("dsadsads", "dassdasdadas",  icon='C:\profile.jpg')
