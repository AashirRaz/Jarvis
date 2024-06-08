# JARVIS 🤖

Jarvis is an open-source Android/IOS build pipeline for seamlessly compiling mobile applications and sending them to your teammates using Skype

## Pre-Requisites for Installation 🛠️

- Python 3
- Powershell 7

## Getting Started 🚀

- After Cloning the project, run the following command to install all required packages

#### On Windows

```bash
pip install -r windows_requirements.txt
```

#### On MacOS

```bash
pip install -r mac_requirements.txt
```

### Diawi Account

- Create a Diawi Account and fill in the credentials in the Credentials.py file
- Go to https://dashboard.diawi.com/profile/api and generate an API Key
- Paste the API Key in the Credentials.py file

- Create a Credentials.py File and structure it as follows

```py
class Credentials:
    SkypeUserName = "Your Skype UserName"
    SkypePassword = "Your Skype Password"
    DiawiEmail = "Your Diawi Email"
    DiawiPassword = "Your Diawi Password"
    DiawiApiKey = "Your Diawi API Key"
    BasePath = r"{Your directory containing all your projects goes here}"
```

## Configuration ⚙️

### Windows

1. Open your Terminal as Administrator
2. Enter the following code into your terminal

```ps1
notepad $PROFILE
```

If you encounter any error regarding missing profiles, Enter the following code and repeat above step

```ps1
New-Item -Path $PROFILE -ItemType File -Force
```

Paste the below code into your notepad file

```ps1
Function init {
    $scriptPath = "{Your Directory Path}\Jarvis\jarvis_build.py"

    Invoke-Expression "python `"$scriptPath`""
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
nano ~/.bash_profile or ~/.zshrc
```

Enter this into your bash_profile

```zsh
alias jarvis_build="python3 {Your Directory Path}/Jarvis/jarvis_build.py"
```

Save changes to your file and exit the text editor

Enter the following into your Terminal to save the changes

```zsh
source ~/.bash_profile
```

## Contributing 🤝

- [Submit a bug report or issue](mailto:syedaashirraza@gmail.com)
- [Contribute code by submitting a pull request](mailto:syedaashirraza@gmail.com)
- [Ask a question](mailto:syedaashirraza@gmail.com)

## Support 🛡️

Jarvis is a something we do in our spare time around our day job, friends, and other hobbies. That means support is "when we get to it". We recognize that sometimes this isn't good enough, especially if you have a production issue. To that end, We [offer paid support and bugfixes](syedaashirraza@gmail.com). A few basic rules before you contact me:

- Changes made to Jarvis are open source.
- We reserve the right to make any changes we desire to the codebase.

Please email me if paid support is something you require, and we can work out the details via email.
