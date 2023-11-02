import os

class SeleniumXpaths:
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
    ImageFolderPath = r"C:\AashirRaza\Scripts\diawiScreenshots"


class WebsiteLink:
    Diawi = "https://www.diawi.com/"


class LoadingState:
    Completed = "100%"

class Skype:
    UserName = "aashir_raza1602@outlook.com"
    Password = "@@$hir123"
    IconPath = r"src\main\res\mipmap-xxxhdpi\ic_launcher_round.png"