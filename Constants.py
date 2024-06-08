from sys import platform

class OS:
    IOS = platform == "darwin"
    WINDOWS = platform == "win32"
    LINXUS = platform == "linux"
class PathConstants:
    AndroidPathAPK = r"app/build/outputs/apk/release/app-release.apk" if OS.IOS else r"app\build\outputs\apk\release\app-release.apk"
    AndroidPathBundle = r"app/build/outputs/bundle/release/app-release.aab" if OS.IOS else r"app\build\outputs\bundle\release\app-release.aab"
    AndroidIconPath =   r"src/main/res/mipmap-xxxhdpi/ic_launcher_round.png" if OS.IOS else  r"src\main\res\mipmap-xxxhdpi\ic_launcher_round.png"
    IosIconPath = r"{0}/Images.xcassets/AppIcon.appiconset/ItunesArtwork@2x.png"
    IosBuildPath = r'build/{0}Build/{0}.ipa'

class DiawiUrls:
    DIAWI_UPLOAD_URL = 'https://upload.diawi.com/'
    DIAWI_CHECK_STATUS_URL = 'https://upload.diawi.com/status'

class BuildPlatforms:
    Android = "Android"
    IOS = "IOS"
    Both = "Both"
