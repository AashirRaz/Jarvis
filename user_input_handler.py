import inquirer
from inquirer.themes import BlueComposure
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
    reactNativeFolders = ["android", "ios", "src"]
    current_directory = os.getcwd()
    project_name = current_directory.split('/')[-1]

    inDirectory = not all(os.path.exists(os.path.join(current_directory, f)) for f in reactNativeFolders)

    if inDirectory:
        questions.append(inquirer.List("DirectoryPath", message="Which application do you want to compile?",choices=getFolderNames()))
    else:
        result.append(project_name)

    if(OS.IOS):
        questions.append(inquirer.List("Platform", message="For which platform do you want to build.", choices=[BuildPlatforms.Both, BuildPlatforms.Android, BuildPlatforms.IOS], default="Both")) 

    questions.append(inquirer.List("BuildType", message="Which build type do you want to build", choices=["release","bundle"], default="release"))
        
    questions.append(inquirer.Checkbox(
            "SkypeContacts", message="Select Skype Contacts to send application to  (Press <space> to select, <tab> to toggle all", choices=skypeContacts
        )),

    ans = inquirer.prompt(questions)

    if inDirectory:
        result.append(ans.get("DirectoryPath"))

    if(OS.IOS):
        result.append(ans.get("Platform"))
    else:
        result.append(BuildPlatforms.Android)
    
    result.append(ans.get("BuildType"))

    for contact in ans.get("SkypeContacts"):
        result.append(contact)

    return result
