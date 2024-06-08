from Constants import OS, PathConstants
from Credentials import Credentials
import os
import subprocess
from SkypeService import SkypeService
from DiawiService import UploadToDiawi
from toast import toast

def android_build(directory_path: str, build_type, sendToWhom, skypeService:SkypeService): 

    # Change to the "android" directory
    android_path = os.path.join(directory_path, "android")
    os.chdir(android_path)

    project_name = directory_path.split('/')[-1]

    if build_type == "release":
        print("\n")
        toast("[5/10]", "Building Android Release APK...")
        subprocess.run(["./gradlew assembleRelease"] if OS.IOS else ["gradlew", "assembleRelease"], shell=True, check=True,  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Determine the package size
        package_path = os.path.join(android_path, PathConstants.AndroidPathAPK)
        package_size = os.path.getsize(package_path) / (1024 * 1024)

        # print("Package size: ", package_size, "MB")
        toast(message=f"Package size: {round(package_size)} MB", type='info')
        toast("[6/10]", "Successfully Built Android Release APK", 'success')

        HasDiawiAccount = bool(Credentials.DiawiEmail) and bool(Credentials.DiawiPassword)
        if package_size < (250 if  HasDiawiAccount else 50):
            UploadToDiawi(sendToWhom, package_path, f"{project_name} APK", skypeService)
        else:
            toast("[6/10]", "Package size is too large to upload to Diawi", 'warning')
            skypeService.SendMsgToSkype(sendToWhom , package_path, f"{package_path} APK")

        # subprocess.run(["./gradlew clean"] if OS.IOS else ["gradlew", "clean"], shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if build_type == "bundle":
        toast("[5/10]", "Building Android Bundle AAB...")

        subprocess.run(["./gradlew bundleRelease"] if OS.IOS else ["gradlew", "bundleRelease"], shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        package_path = os.path.join(android_path, PathConstants.AndroidPathBundle)

        toast("[6/10]", "Successfully Built Android Bundle AAB", 'success')
        toast("[7/10]", "Sending Message to Skype...")
        skypeService.SendMsgToSkype(sendToWhom , package_path, f"{project_name} AAB")
        os.remove(package_path)
        toast("[8/10]", "Successfully Sent Message to Skype", 'success')
