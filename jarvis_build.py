
import os
import subprocess
import sys
import sendToSkype
import uploadToDiawi

def jarvis_build(directory_path, build_type, sendToWhom): 
    try:
        
        base_path = r"C:\AashirRaza\Koderlabs"
        full_path = os.path.join(base_path, directory_path)

        print("-------> Navigating to directory")

        os.chdir(full_path)

        print("-------> Directory navigation successful.\n")


        if build_type == "release":
            print("-------> Making release build\n")

            # Change to the "android" directory
            android_path = os.path.join(full_path, "android")
            os.chdir(android_path)

            subprocess.run(["gradlew", "assembleRelease"], shell=True, check=True)

            # Determine the package size
            package_path = os.path.join(
                android_path,
                r"app\build\outputs\apk\release\app-release.apk",
            )


            package_size = os.path.getsize(package_path) / (1024 * 1024)

            print(f"Package size is {package_size} MB")

            if package_size < 60:
                print("Uploading build to Diawi...")

                uploadToDiawi.UploadToDiawi(sendToWhom, package_path, directory_path)
                # sendToSkype.SendMsgToSkype(sendToWhom , package_path, "{} build".format(directory_path))
                
                # Place your Diawi upload logic here
                # You might use requests to upload the build to Diawi

            else:
                sendToSkype.SendMsgToSkype(sendToWhom , package_path, "{} build".format(directory_path))
                print(f"Build package is too large to upload to Diawi ({package_size} MB).")

        if build_type == "bundle":
            print("Making bundle build...")

            # Change to the "android" directory
            android_path = os.path.join(full_path, "android")
            os.chdir(android_path)

            subprocess.run(["gradlew", "bundleRelease"], shell=True, check=True)

            # Determine the package size
            package_path = os.path.join(
                android_path,
                r"app\build\outputs\bundle\release\app-release.aab",
            )

            sendToSkype.SendMsgToSkype(sendToWhom , package_path, "{} build".format(directory_path))
            print(f"Build package is too large to upload to Diawi ({package_size} MB).")

    except:
        pass



if __name__ == "__main__":
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


