from Credentials import Credentials
import os
import subprocess
from SkypeService import SkypeService
from DiawiService import UploadToDiawi
import shutil
from toast import toast


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

def ios_build(directory_path, build_type, send_to_whom, files: dict[str, str], skype_service: SkypeService):
    # Initiates the build process for iOS or Android based on the build type.

    # Change to the "ios" directory
    ios_path = os.path.join(directory_path, "ios")
    os.chdir(ios_path)


    if build_type == "release":

        # Remove .xcode.env.local file if exists
        xcode_env_local_path = os.path.join(ios_path, ".xcode.env.local")
        if os.path.exists(xcode_env_local_path):
            toast(message="Removing .xcode.env.local file", type='info')
            os.remove(xcode_env_local_path)

        toast(message=f"Found Workspace and Project Files in the directory {files['proj']}, {files['workspace']}", type='info')
        name = files["proj"].split(".")[0]

        try:
            # List the schemes in the project
            toast("[5/10]","Building IOS IPA Build...")
            result = subprocess.run(["xcodebuild", "-list", '-project', f'{files["proj"]}'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            schemes = extract_schemes(result.stdout)

            # Archive the project
            # archive_command = f"xcodebuild -workspace {files.get('workspace')} -scheme {schemes[0]} -configuration 'Release' -sdk iphoneos archive -archivePath ${{PWD}}/build/{name}.xcarchive"
            archive_command = [
                "xcodebuild",
                "-workspace", files.get('workspace'),
                "-scheme", schemes[0],
                "-configuration", "Release",
                "-sdk", "iphoneos",
                "archive",
                "-archivePath", f"{ios_path}/build/{name}.xcarchive"
            ]
            subprocess.run(archive_command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            toast(message="Successfully archived the project", type='info')

            # Export the archive
            export_options_plist = '/Users/aashirraza/Desktop/Tests/Jarvis/exportOption.plist'
            shutil.copy(export_options_plist, ios_path)
            
            # export_command = f"xcodebuild -exportArchive -archivePath {ios_path}/build/{name}.xcarchive -exportOptionsPlist exportOption.plist -exportPath {ios_path}/build/{name}Build"
            export_command = [
                "xcodebuild",
                "-exportArchive",
                "-archivePath", f"{ios_path}/build/{name}.xcarchive",
                "-exportOptionsPlist", "exportOption.plist",
                "-exportPath", f"{ios_path}/build/{name}Build"
            ]
            subprocess.run(export_command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            os.remove(os.path.join(ios_path, 'exportOption.plist'))
            toast("[6/10]", "Successfully Build and Exported IOS IPA Build", 'success')

            # Determine package size and upload to Diawi if appropriate
            package_path = os.path.join(ios_path, f"build/{name}Build/{name}.ipa")
            package_size = os.path.getsize(package_path) / (1024 * 1024)
            
            toast(message=f"Package size: {round(package_size)} MB", type='info')

            HasDiawiAccount = bool(Credentials.DiawiEmail) and bool(Credentials.DiawiPassword)
            if package_size < (250 if HasDiawiAccount else 50):
                UploadToDiawi(send_to_whom, package_path, f"{name} IPA", skype_service)
            else:
                toast("[6/10]", "Package size is too large to upload to Diawi", 'warning')
                skype_service.SendMsgToSkype(send_to_whom, package_path, f"{name} build")

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

