from Constants import OS, BuildPlatforms
from SkypeService import SkypeService
from DiawiService import DiawiService
from android_build import android_build
from user_input_handler import HandleUserInput
from ios_build import ios_build
from reusableFunctions import writeJarvisArt
# from threading import Thread

# def run_android_build(directory_path, build_type, send_to_whom, skype_service, diawi_service):
#     # Runs the Android build process.
#     android_build(directory_path, build_type, send_to_whom, skype_service, diawi_service)

# def run_ios_build(directory_path, build_type, send_to_whom, skype_service, diawi_service):
#     # Runs the iOS build process.
#     ios_build(directory_path, build_type, send_to_whom, skype_service, diawi_service)


if __name__ == "__main__":
    skypeService = SkypeService()
    diawiService = DiawiService()

    writeJarvisArt()

    result = HandleUserInput(skypeService.getContacts())

    directory_path = result[0]
    platform = result[1]
    build_type = result[2]
    sendToWhom = result[3:]

    match platform:
        case BuildPlatforms.Android:
            android_build(directory_path, build_type, sendToWhom, skypeService, diawiService)
        case BuildPlatforms.IOS:
            ios_build(directory_path, build_type, sendToWhom, skypeService, diawiService)
        case BuildPlatforms.Both:
            # Create threads for Android and iOS builds
            # args = (directory_path, build_type, sendToWhom, skypeService, diawiService)
            # android_thread = Thread(target=run_android_build, args=args)
            # ios_thread = Thread(target=run_ios_build, args=args)

            # # Start the threads
            # android_thread.start()
            # ios_thread.start()

            # # Wait for both threads to complete
            # android_thread.join()
            # ios_thread.join()

            

            android_build(directory_path, build_type, sendToWhom, skypeService, diawiService)
            ios_build(directory_path, build_type, sendToWhom, skypeService, diawiService)


