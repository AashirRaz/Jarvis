import os
from sys import platform

class OS:
    IOS = platform == "darwin"
    WINDOWS = platform == "win32"
    LINXUS = platform == "linux"
class PathConstants:
    BasePath = r"/Users/aashirraza/Desktop/Koderlabs"
    AndroidPathAPK = r"app/build/outputs/apk/release/app-release.apk" if OS.IOS else r"app\build\outputs\apk\release\app-release.apk"
    AndroidPathBundle = r"app/build/outputs/bundle/release/app-release.aab" if OS.IOS else r"app\build\outputs\bundle\release\app-release.aab"
    AndroidIconPath =   r"src/main/res/mipmap-xxxhdpi/ic_launcher_round.png" if OS.IOS else  r"src\main\res\mipmap-xxxhdpi\ic_launcher_round.png"
    IosIconPath = r"{0}/Images.xcassets/AppIcon.appiconset/ItunesArtwork@2x.png"
class SeleniumXpaths:
    LoginPageButton = r"/html/body/header/div/div[2]/div/span[1]/a"
    EmailAddress = r"/html/body/div[1]/div/form/div[2]/input"
    Password = r"/html/body/div[1]/div/form/div[3]/input"
    LoginButton = r"/html/body/div[1]/div/form/div[4]/input"
    FileUploadXpath = "/html/body/section/section[2]/div[1]/form/div[1]/div[2]/input"
    LoadingText = "/html/body/section/section[2]/div[1]/form/div[1]/div[1]/div/div/div/ul/li/div[3]"
    SubmitButtonXpath = "/html/body/section/section[2]/div[1]/form/div[3]/input"
    UrlLinkElement = r"/html/body/section/section[2]/div[1]/div/div[1]/div[2]/a"
    ImageElementXpath = r'//*[@id="main-container"]/section[2]/div[1]/div/div[2]/img'

class Settings:
    HEADLESSMODE = "--headless"
    LOG_LEVEL3 = "--log-level=3"
    IGNORE_CERTIFICATE_ERRORS = "--ignore-certificate-errors"

class SystemPaths:
    ImageFolderPath = r"/Users/aashirraza/Desktop/Tests/Jarvis/temp/app_qrcode.png"
    ImageDirectoryPath = r"/Users/aashirraza/Desktop/Tests/Jarvis/temp"

class WebsiteLink:
    Diawi = "https://www.diawi.com/"

class LoadingState:
    Completed = "100%"

class BuildPlatforms:
    Android = "Android"
    IOS = "IOS"
    Both = "Both"
