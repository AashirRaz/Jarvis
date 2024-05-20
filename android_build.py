from Constants import OS, PathConstants
from reusableFunctions import jarvis_init
from Credentials import Credentials
import os
import subprocess
from SkypeService import SkypeService
from DiawiService import DiawiService

def android_build(directory_path, build_type, sendToWhom, skypeService:SkypeService): 
    try:
        # Change to the "android" directory
        android_path = os.path.join(directory_path, "android")
        os.chdir(android_path)

        if build_type == "release":
            
            subprocess.run(["./gradlew assembleRelease"] if OS.IOS else ["gradlew", "assembleRelease"], shell=True, check=True)

            # Determine the package size
            package_path = os.path.join(android_path, PathConstants.AndroidPathAPK)
            package_size = os.path.getsize(package_path) / (1024 * 1024)

            print("Package size: ", package_size, "MB")

            if package_size < (250 if Credentials.HasDiawiAccount else 50):
                print("Uploading build to Diawi...")
                diawiService = DiawiService()
                diawiService.UploadToDiawi(sendToWhom, package_path, f"{directory_path} Apk", skypeService)
            else:
                print('Package size is too large to upload to Diawi')
                skypeService.SendMsgToSkype(sendToWhom , package_path, "{} build".format(directory_path))

        if build_type == "bundle":
            print("Making bundle build...")

            subprocess.run(["./gradlew bundleRelease"] if OS.IOS else ["gradlew", "bundleRelease"], shell=True, check=True)
            package_path = os.path.join(android_path, PathConstants.AndroidPathBundle)
            skypeService.SendMsgToSkype(sendToWhom , package_path, "{} build".format(directory_path))
    except:
        pass