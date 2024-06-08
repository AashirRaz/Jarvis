from SkypeService import SkypeService
from user_input_handler import HandleUserInput
from reusableFunctions import jarvis_logo
from build_handler import create_build
import sys

if __name__ == "__main__":
    sys.tracebacklimit = 0
    
    jarvis_logo()

    skypeService = SkypeService()
    result = HandleUserInput(skypeService.getContacts())

    create_build(result, skypeService)


