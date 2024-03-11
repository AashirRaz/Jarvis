
import os
import subprocess
import sys
import sendToSkype
import uploadToDiawi
from Constants import OS, PathConstants
from reusableFunctions import jarvis_init



def jarvis_build(directory_path, build_type, sendToWhom): 
    try: 
        full_path:str = jarvis_init(directory_path)

        if build_type == "release":
            # Change to the "android" directory
            android_path = os.path.join(full_path, "android")
            os.chdir(android_path)

            subprocess.run(["./gradlew assembleRelease"] if OS.IOS else ["gradlew", "assembleRelease"], shell=True, check=True)

            # Determine the package size
            package_path = os.path.join(android_path, PathConstants.AndroidPathAPK)

            package_size = os.path.getsize(package_path) / (1024 * 1024)

            if package_size < 250:
                print("Uploading build to Diawi...")
                uploadToDiawi.UploadToDiawi(sendToWhom, package_path, directory_path)
            else:
                sendToSkype.SendMsgToSkype(sendToWhom , package_path, "{} build".format(directory_path))

        if build_type == "bundle":
            print("Making bundle build...")

            android_path = os.path.join(full_path, "android")
            os.chdir(android_path)

            subprocess.run(["./gradlew bundleRelease"] if OS.IOS else ["gradlew", "bundleRelease"], shell=True, check=True)

            package_path = os.path.join(android_path, PathConstants.AndroidPathBundle)

            sendToSkype.SendMsgToSkype(sendToWhom , package_path, "{} build".format(directory_path))

    except:
        pass



if __name__ == "__main__":
    sendToSkype.init_skype()

    print("\n")
    print("""
                     .B@@@@@@!  ?###&&&@@@@   . ^5GB#&&&@@@@@@&B7 !@@@@@@7  J@@@@@&:JGGB#&G    :!YPB&&@@@&#G 
                     !@@@@@@P. ^&@@@@@@@@@@     J@@@@@@@@@@@@@@@@ !@@@@@@^ :&@@@@@7:@@@@@@? :?G&@@@@@@@@@@@@&
                     G@@@@@@~  P@@@@@J#@@@@     G@@@@@#JJJY5#@@@@ 7@@@@@#. ?@@@@@B.J@@@@@#.7#@@@@@@GJ7P@@@@@@
                    ^@@@@@@P  ?@@@@@P:&@@@@    ^@@@@@@J    :G@@@# J@@@@@P .#@@@@@~ B@@@@@Y?@@@@@@@J   :##G5J7
                    Y@@@@@@~ :&@@@@@^~@@@@@    J@@@@@&: .~5&@@@B^ 5@@@@@? 7@@@@@P !@@@@@&^B@@@@@@@@     
                   .#@@@@@G  5@@@@@5 ?@@@@@   .#@@@@@B?P#@@@@@5:  G@@@@@~ G@@@@@^ P@@@@@P ?@@@@@@@@@@
                   7@@@@@@! !@@@@@&^ 5@@@@@   7@@@@@@@@@@@@#Y^    #@@@@&:~@@@@@5 ^@@@@@@~   P&@@@@@@@@@B     
                   G@@@@@B .#@@@@@J  B@@@@@   P@@@@@@@@@@@J       &@@@@B P@@@@&: Y@@@@@B     ^?G@@@@@@@@@
                  ^&@@@@@? Y@@@@@&7~7&@@@@@  :&@@@@@?P@@@@#~      @@@@@5^@@@@@J :&@@@@@?        ~J#@@@@@@#   
                  Y@@@@@# ~@@@@@@@@@@@@@@@@  J@@@@@#.~@@@@@#^     @@@@@7Y@@@@#. ?@@@@@#:  ^^      ^&@@@@@@
              JJ!J@@@@@@7 B@@@@@@BBB#@@@@@@  #@@@@@Y  P@@@@@#:    @@@@@P&@@@@? .B@@@@@Y  !&&57^   Y@@@@@@G    
             Y@@@@@@@@@P Y@@@@@@?   Y@@@@@@ !@@@@@@~  :&@@@@@B:   @@@@@@@@@@B. 7@@@@@@~ 7@@@@@@&&@@@@@@@#
            Y@@@@@@@@@P ~@@@@@@B    G@@@@@@ P@@@@@B   J@@@@@@5   t@@@@@@@@@? .B@@@@@G  #@@@@@@@@@@@@@&Y 
            JG&@@@@&B?  G&##BGG~   :#@&#BBP &&#BP5~    .GB5J!^:  @@@&&#BBG5. 7@@&&##7   7P#@@@@@@&B57   
    """)

    print("-------> Executing Your Command", sys.argv)

    directory_path = sys.argv[1]
    build_type = sys.argv[2]
    sendToWhom = sys.argv[3:]

    jarvis_build(directory_path, build_type, sendToWhom)


