from reusableFunctions import jarvis_init, notification
from Credentials import Credentials
import os
import subprocess
from SkypeService import SkypeService
from DiawiService import DiawiService
import shutil


def extract_schemes(output:str):
    schemes = []
    scheme_section = False

    for line in output.splitlines():
        line = line.strip()
        if line == "Schemes:":
            scheme_section = True
            continue
        if scheme_section:
            if line:
                schemes.append(line)
            else:
                break  # Stop if we hit an empty line after schemes

    return schemes

def find_ios_required_folder(directory_path: str):
    result = {"proj": "", "workspace": ""}
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isdir(item_path):
            if item.endswith('.xcodeproj'):
                result["proj"] = item
            elif item.endswith('.xcworkspace'):
                result["workspace"] = item
    return result

def ios_build(directory_path, build_type, send_to_whom, skype_service: SkypeService, diawi_service: DiawiService):
    # Initiates the build process for iOS or Android based on the build type.
    try:
        full_path = jarvis_init(directory_path)

        # Change to the "ios" directory
        ios_path = os.path.join(full_path, "ios")
        os.chdir(ios_path)

        if build_type == "release":
            print("Making release build...", ios_path)

            # Remove .xcode.env.local file if exists
            xcode_env_local_path = os.path.join(ios_path, ".xcode.env.local")
            if os.path.exists(xcode_env_local_path):
                print("Removing .xcode.env.local file")
                os.remove(xcode_env_local_path)

            # Find required iOS folders
            files = find_ios_required_folder(ios_path)

            print("Project:", files)

            name = files["proj"].split(".")[0]

            try:
                # List the schemes in the project
                list_command = f"xcodebuild -list -project {files['proj']}"
                print(list_command)
                result = subprocess.run(["xcodebuild", "-list", '-project', f'{files["proj"]}'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                print(result.stdout)
                schemes = extract_schemes(result.stdout)

                # Archive the project
                archive_command = f"xcodebuild -workspace {files.get("workspace")} -scheme {schemes[0]} -configuration 'Release' -sdk iphoneos archive -archivePath ${{PWD}}/build/{name}.xcarchive"
                print(archive_command)
                subprocess.run(archive_command, check=True, shell=True)

                # Export the archive
                export_options_plist = '/Users/aashirraza/Desktop/Tests/Jarvis/exportOption.plist'
                shutil.copy(export_options_plist, ios_path)
                
                export_command = f"xcodebuild -exportArchive -archivePath ${{PWD}}/build/{name}.xcarchive -exportOptionsPlist exportOption.plist -exportPath ${{PWD}}/build/{name}Build"

                subprocess.run(export_command, check=True, shell=True)
                os.remove(os.path.join(ios_path, 'exportOption.plist'))

                # Determine package size and upload to Diawi if appropriate
                package_path = os.path.join(ios_path, f"build/{name}Build/{name}.ipa")
                package_size = os.path.getsize(package_path) / (1024 * 1024)
                print("Package size:", package_size, "MB")

                if package_size < (250 if Credentials.HasDiawiAccount else 50):
                    print("Uploading build to Diawi...")
                    diawi_service.UploadToDiawi(send_to_whom, package_path, f"{directory_path} IPA", skype_service, name=name)
                else:
                    print('Package size is too large to upload to Diawi')
                    skype_service.SendMsgToSkype(send_to_whom, package_path, f"{directory_path} build")

                # Remove the build directory
                build_path = os.path.join(ios_path, "build")
                os.remove(build_path)

            except subprocess.CalledProcessError as e:
                print(f"Command failed with exit code {e.returncode}")
                print(e.stderr)
            except FileNotFoundError:
                print("The xcodebuild command is not found. Make sure Xcode is installed and xcodebuild is in your PATH.")

        elif build_type == "bundle":
            print("No bundle build for iOS")

    except Exception as e:
        print(f"An error occurred: {e}")
