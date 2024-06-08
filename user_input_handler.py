from Constants import OS, BuildPlatforms
import os
from InquirerPy import inquirer
from Credentials import Credentials


def getFolderNames() -> list[str]:
    folderNames = []
    base_path = Credentials.BasePath
    
    for path in os.listdir(base_path):
        full_path = os.path.join(base_path, path)
        if os.path.isdir(full_path):
            android_path = os.path.join(full_path, "android")
            ios_path = os.path.join(full_path, "ios")
            if os.path.isdir(android_path) and os.path.isdir(ios_path):
                folderNames.append(path)
    
    return folderNames


def HandleUserInput(skypeContacts:list[str]) -> list[str]:
    result = []
    reactNativeFolders = ["android", "ios", "src"]
    current_directory = os.getcwd()
    project_name = current_directory.split('/')[-1]

    inDirectory = not all(os.path.exists(os.path.join(current_directory, f)) for f in reactNativeFolders)

    if inDirectory:
        DirectoryPath = inquirer.select(
            message="Which application do you want to compile?",
            choices=getFolderNames(),
            ).execute()
        result.append(DirectoryPath)
    else:
        result.append(project_name)

    if(OS.IOS):
        Platform = inquirer.select(
            message="Which platform do you want to compile for?",
            choices=[BuildPlatforms.Both, BuildPlatforms.Android, BuildPlatforms.IOS],
            default=BuildPlatforms.Both
            ).execute()
        result.append(Platform)
    else:
        result.append(BuildPlatforms.Android)


    BuildType = inquirer.select(
        message="Which build type do you want to compile?",
        choices=["release","bundle"],
        default="release"
        ).execute()
    
    result.append(BuildType)

    SkypeContacts = inquirer.fuzzy(
        message="Select Skype Contacts to send application to  (Press <tab> to select)",
        choices=skypeContacts,
        multiselect=True,
        validate=lambda result: len(result) > 0,
        invalid_message="minimum 1 selections",
    ).execute()


    for contact in SkypeContacts:
        result.append(contact)

    return result