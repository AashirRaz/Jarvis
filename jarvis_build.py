from DiawiService import DiawiService
from SkypeService import SkypeService
from user_input_handler import HandleUserInput
from reusableFunctions import jarvis_logo
from build_handler import create_build
import sys
from bs4 import MarkupResemblesLocatorWarning
import warnings
from yaspin import yaspin
import time


if __name__ == "__main__":
    sys.tracebacklimit = 0
    warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)
    jarvis_logo()

    skypeService = SkypeService()
    diawiService = DiawiService(skypeService)
    result = HandleUserInput(skypeService.getContacts())

    create_build(result, skypeService)


