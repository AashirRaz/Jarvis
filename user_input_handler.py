import inquirer
from inquirer.themes import GreenPassion, BlueComposure
from Constants import PathConstants, OS, BuildPlatforms
import os


def getFolderNames() -> list[str]:
    folderNames = []
    for path in os.listdir(PathConstants.BasePath):
        if os.path.isdir(os.path.join(PathConstants.BasePath, path)):
            folderNames.append(path)
    return folderNames

def HandleUserInput(skypeContacts:list[str]) -> list[str]:
    questions = []
    result = []

    questions.append(inquirer.List("DirectoryPath", message="Which application do you want to compile?",choices=getFolderNames())),

    if(OS.IOS):
        questions.append(inquirer.List("Platform", message="For which platform do you want to build", choices=[BuildPlatforms.Android, BuildPlatforms.IOS, BuildPlatforms.Both], default="Both")) 

    questions.append(inquirer.List("BuildType", message="Which build type do you want to build", choices=["bundle", "release"], default="bundle"))
        
    questions.append(inquirer.Checkbox(
            "SkypeContacts", message="Select Skype Contacts to send application to", choices=skypeContacts
        )),

    ans = inquirer.prompt(questions, theme=BlueComposure())

    result.append(ans.get("DirectoryPath"))
    if(OS.IOS):
        result.append(ans.get("Platform"))
    else:
        result.append(BuildPlatforms.Android)
    
    result.append(ans.get("BuildType"))

    for contact in ans.get("SkypeContacts"):
        result.append(contact)

    return result


