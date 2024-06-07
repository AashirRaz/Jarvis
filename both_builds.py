from threading import Thread
from android_build import android_build
from ios_build import ios_build

def multithreaded_build(directory_path, build_type, send_to_whom,files,  skype_service):
    # Initiates the build process for iOS or Android based on the build type.
    android_thread = Thread(target=android_build, args=(directory_path, build_type, send_to_whom, skype_service))
    ios_thread = Thread(target=ios_build, args=(directory_path, build_type, send_to_whom, files, skype_service))

    # Start the threads
    android_thread.start()
    ios_thread.start()

    # Wait for both threads to complete
    android_thread.join()
    ios_thread.join()


def SingleThreadedBuild(directory_path, build_type, send_to_whom, files, skype_service):
    android_build(directory_path, build_type, send_to_whom, skype_service)
    ios_build(directory_path, build_type, send_to_whom, files, skype_service)  