
import os
import subprocess
import sys
from Constants import OS
from reusableFunctions import jarvis_init, jarvis_logo

if __name__ == "__main__":
    jarvis_logo()

    directory_path = sys.argv[1]

    jarvis_init(directory_path)

    subprocess.run(["code ."] if OS.IOS else ["code", "."],check=True)
    