from SkypeService import SkypeService
from DiawiService import DiawiService
from user_input_handler import HandleUserInput
from reusableFunctions import jarvis_logo
from build_handler import create_build

if __name__ == "__main__":
    skypeService = SkypeService()
    diawiService = DiawiService()

    jarvis_logo()

    result = HandleUserInput(skypeService.getContacts())

    create_build(result, skypeService, diawiService)


