
import os
import subprocess
import sys
from Constants import OS, PathConstants
from reusableFunctions import jarvis_init

def jarvis_open(directory_path): 

    jarvis_init(directory_path)

    subprocess.run(["code ."] if OS.IOS else ["code", "."], shell=True, check=True)

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
    
    jarvis_open(directory_path)