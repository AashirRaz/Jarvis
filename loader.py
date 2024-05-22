import ctypes
import os
import time
from threading import Thread
from loaders import SpinningLoader
import sys

class Loader:
    def __init__(self) -> None:
        self.thread = None

    def start(self, stepCount, message):
        if not self.thread:
            thread = Thread(target=self.printLoader, args=(stepCount, message))
            thread.daemon = True
            self.thread = thread
            self.thread.start()
            return True
        else:
            return False
        
    def printLoader(self, stepCount, message):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(stepCount + " " + message, end='')
        count = 0
        while True:
            while count <= 3:
                time.sleep(1)
                print('.', end='', flush=True)
                count += 1
            count = 0
            os.system('cls' if os.name == 'nt' else 'clear')
            print(stepCount + " " + message, end='')


    def stop(self, message:str) -> None:
        if self.thread:
            self.terminate()
            self.thread = None
            os.system('cls' if os.name == 'nt' else 'clear')
            print(message)
            return True
        else:
            sys.stdout.write("%s thread not started." % str(self))
            return False

    def terminate(self):
        if self.thread:
            if not self.thread.is_alive():
                return
            exc = ctypes.py_object(SystemExit)
            res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
                ctypes.c_long(self.thread.ident), exc)
            if res == 0:
                raise ValueError("nonexistent thread id")
            elif res > 1:
                ctypes.pythonapi.PyThreadState_SetAsyncExc(self.thread.ident, None)
                raise SystemError("PyThreadState_SetAsyncExc failed")
            else:
                return
        else:
            raise ValueError("No thread to terminate")



loader = Loader()

loader.start("1/4", "Making release build")
time.sleep(5)
loader.stop("Successfully made release build")