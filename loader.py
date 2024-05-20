import os
import time
from threading import Thread

class Loader:
    def __init__(self) -> None:
        self.state = False

    def start(self, stepCount, message):
        self.state = True
        os.system('cls' if os.name == 'nt' else 'clear')
        print(stepCount + " " + message, end='')
        while self.state:
            count = 0
            while count <= 3:
                time.sleep(1)
                print('.', end='', flush=True)
                count += 1

            count = 0
            os.system('cls' if os.name == 'nt' else 'clear')
            print(stepCount + " " + message, end='')

    def loader_stop(self, message:str) -> None:
        self.state = False
        print(message)
    






loader = Loader()


startLoader = Thread(target=loader.start, args=("1/4", "Complete!"))
stoploader = Thread(target=loader.loader_stop, args=("Complete!"))

startLoader.start()
time.sleep(5)
stoploader.start()










# timer = 0
# loading = "Loading: [----------]"
# backtrack = '\b'*len(loading)

# while timer < 11:
#     sys.stdout.write(backtrack + loading)
#     sys.stdout.flush()
#     loading = loading.replace("-","=",1)
#     time.sleep(1)
#     timer += 1
# time.sleep(1)
# sys.stdout.write(backtrack)
# print (loading+" Complete!")

