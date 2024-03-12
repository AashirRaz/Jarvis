# JARVIS

Jarvis is an open-source Android/IOS build pipeline for seamlessly compiling mobile applications and sending them to your teammates using Skype

## Pre Requisites for Installation

Python 3
ChromeDriver
Powershell 7

## Configuration

### Windows

Open your Terminal as Administrator
Enter the following into your terminal

```sh
notepad $PROFILE
```

if you encounter any error regarding missing profiles, Enter the following code and repeat above step

```sh
New-Item -Path $PROFILE -ItemType File -Force
```

Paste the below code into your

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

    $directory = 'E:\Personal Programming'

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

    $scriptPath = "E:\Personal Programming\Jarvis\a.py"
    $arguments = "$directoryName $type $namesToSend"

    Invoke-Expression "python `"$scriptPath`" $arguments"
}

Set-Alias -Name jarvis_build -Value init
```

## Contributing

- [Submit a bug report or issue](<https://github.com/rianjs/ical.net/wiki/Filing-a-(good)-bug-report>)
- [Contribute code by submitting a pull request](<https://github.com/rianjs/ical.net/wiki/Contributing-a-(good)-pull-request>)
- [Ask a question](https://github.com/rianjs/ical.net/issues)

## Support

ical.net is a something I do in my spare time around my family, day job, friends, and other hobbies. That means support is "when I get to it". I recognize that sometimes this isn't good enough, especially if you have a production issue. To that end, I [offer paid support and bugfixes](http://rianjs.net/consulting). A few basic rules before you contact me:

- Changes made to the ical.net library are open source.
- You do not own the changes I make to the library.
- Congruence with my vision for the future for ical.net is required. That means I won't do things like add Exchange interop, or take dependencies on third-party libraries that benefit only your use case.
- New versions of the library that result from changes made will be published on nuget for others to consume.

Please email me if paid support is something you require, and we can work out the details via email.

## Creative Commons

iCal.NET logo adapted from [Love Calendar](https://thenounproject.com/term/love-calendar/116866/) By Sergey Demushkin, RU
