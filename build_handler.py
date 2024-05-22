import os
from android_build import android_build
from ios_build import find_ios_required_folder, ios_build
from both_builds import multithreaded_build
import SkypeService
from Constants import OS, BuildPlatforms, PathConstants
from reusableFunctions import jarvis_init

def create_build(result:list[str], skypeService:SkypeService) -> None:
    directory_path = jarvis_init(result[0])
    platform = result[1]
    build_type = result[2]
    sendToWhom = result[3:]

    match platform:
        case BuildPlatforms.Android:
            android_build(directory_path, build_type, sendToWhom, skypeService)
        case BuildPlatforms.IOS:
            ios_build(directory_path, build_type, sendToWhom, skypeService)
        case BuildPlatforms.Both:
            multithreaded_build(directory_path, build_type, sendToWhom, skypeService)

    iosPath = os.path.join(directory_path, "ios" if platform == BuildPlatforms.IOS else "android")
    files = find_ios_required_folder(iosPath)
    print("Project:", files)
    name = files["proj"].split(".")[0]

    extendedPath = PathConstants.IosIconPath.format(name) if OS.IOS else PathConstants.AndroidIconPath
    appIcon = os.path.join(iosPath, extendedPath)
    print(appIcon, name)
    # notification("Jarvis: App Successfully Sent via Skype", f"Jarvis has successfully built and sent the app to {[contact for contact in contacts]} via Skype Succesfully...", appIcon, path)

        