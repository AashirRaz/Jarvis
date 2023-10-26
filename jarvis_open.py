
import os
import subprocess
import sys

def jarvis_open(directory_path, action): 

    base_path = r"C:\AashirRaza\Koderlabs"
    full_path = os.path.join(base_path, directory_path)

    print("-------> Navigating to directory")

    os.chdir(full_path)

    if action == "open":
        print("-------> Starting code")
        subprocess.run(["code", "."], shell=True, check=True)
                
    print("-------> Directory navigation successful.\n")


if __name__ == "__main__":
    print("\n")
    print("******************************************************************************************")
    print("******************************************************************************************")
    print("***********************|                                         |************************")
    print("***********************|           Welcome to JARVIS             |************************")
    print("***********************|                                         |************************")
    print("******************************************************************************************")
    print("******************************************************************************************\n")
    print("-------> Executing Your Command")

    directory_path = sys.argv[1]
    action = sys.argv[2]
    
    jarvis_open(directory_path, action)