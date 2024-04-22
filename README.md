# JARVIS

Jarvis is an open-source Android/IOS build pipeline for seamlessly compiling mobile applications and sending them to your teammates using Skype

## Pre-Requisites for Installation

- Python 3
- ChromeDriver https://chromedriver.chromium.org/downloads
- Powershell 7

## Getting Started

- After Cloning the project, run the Install.py file to install all required packages
- Create a Credentials.py File and structure it as follows

```py
class Credentials:
    SkypeUserName = "Your Skype UserName"
    SkypePassword = "Your Skype Password"
    HasDiawiAccount = False
    DiawiEmail = ""
    DiawiPassword = ""
```

- In the Constants.py file replace the following data

```py
class PathConstants:
    BasePath = r"{Your directory containing all your projects goes here}"
    AndroidPathAPK = r"app/build/outputs/apk/release/app-release.apk" if OS.IOS else r"app\build\outputs\apk\release\app-release.apk"
    AndroidPathBundle = r"app/build/outputs/bundle/release/app-release.aab" if OS.IOS else r"app\build\outputs\bundle\release\app-release.aab"
    IconPath = r"src/main/res/mipmap-xxxhdpi/ic_launcher_round.png" if OS.IOS else  r"src\main\res\mipmap-xxxhdpi\ic_launcher_round.png"


class SystemPaths:
    ImageFolderPath = r"{Path to folder where you want to store temporary Diawi QR Screenshots}"
```

## Configuration

### Windows

Open your Terminal as Administrator and enter the following code into your terminal

```ps1
notepad $PROFILE
```

If you encounter any error regarding missing profiles, Enter the following code and repeat above step

```ps1
New-Item -Path $PROFILE -ItemType File -Force
```

Paste the below code into your notepad file

```ps1
function Get-FileNames {
    param (
        [string]$DirectoryPath
    )

    Set-Location -Path $DirectoryPath

    $files = Get-ChildItem -Directory

    # Output the names of the files
    $files | ForEach-Object { "'$($_.Name)'" }
}

function Get-FileNamesCompleter {
    param($commandName, $parameterName, $wordToComplete, $commandAst, $fakeBoundParameter)

    $directory = 'Your Directory Path Goes Here'

    $files = Get-FileNames -DirectoryPath $directory

    $files | Where-Object { $_ -like "$wordToComplete*" }
}


Function init {
    [CmdletBinding()]
    param (
	[Parameter(Mandatory)]
	[ArgumentCompleter({ Get-FileNamesCompleter @args })]
        [string]$directoryName,

	[Parameter(Mandatory=$true)]
	[ValidateSet('release', 'bundle')]
	$type,

	[Parameter(Mandatory)]
        [string[]]
	$namesToSend
    )

    $scriptPath = "Your Directory Path\Jarvis\jarvis_build.py"
    $arguments = "$directoryName $type $namesToSend"

    Invoke-Expression "python `"$scriptPath`" $arguments"
}

Set-Alias -Name jarvis_build -Value init
```

Save the Notepad file and Restart your terminal to Save Changes

Copy the main directory location of your project and put in the PATH Environment Variable

### MacOS

Open your terminal and Enter the following code into your terminal

```zsh
cd ~
```

Then enter this, your Bash Profile with open inside of a text editor

```zsh
nano ~/.bash_profile
```

OR if you dont have Bash Profile

```zsh
nano ~/.zshrc
```

Enter this into your bash_profile

```zsh
alias jarvis_build="python3 {Path to your python file}"
```

Save changes to your file and exit the text editor

Enter the following into your Terminal to save the changes

```zsh
source ~/.bash_profile
```

## Contributing

- [Submit a bug report or issue](mailto:syedaashirraza@gmail.com)
- [Contribute code by submitting a pull request](mailto:syedaashirraza@gmail.com)
- [Ask a question](mailto:syedaashirraza@gmail.com)

## Support

Jarvis is a something we do in our spare time around our day job, friends, and other hobbies. That means support is "when we get to it". We recognize that sometimes this isn't good enough, especially if you have a production issue. To that end, We [offer paid support and bugfixes](syedaashirraza@gmail.com). A few basic rules before you contact me:

- Changes made to Jarvis are open source.
- We reserve the right to make any changes we desire to the codebase.

Please email me if paid support is something you require, and we can work out the details via email.
