from android_build import android_build
from ios_build import ios_build
from both_builds import multithreaded_build
import SkypeService
import DiawiService
from Constants import BuildPlatforms

def create_build(result:list[str], skypeService:SkypeService, diawiService:DiawiService) -> None:
    directory_path = result[0]
    platform = result[1]
    build_type = result[2]
    sendToWhom = result[3:]

    match platform:
        case BuildPlatforms.Android:
            android_build(directory_path, build_type, sendToWhom, skypeService, diawiService)
        case BuildPlatforms.IOS:
            ios_build(directory_path, build_type, sendToWhom, skypeService, diawiService)
        case BuildPlatforms.Both:
            multithreaded_build(directory_path, build_type, sendToWhom, skypeService, diawiService)