"""
  This program is designed to create
  and animate a simple loading animation.
"""

from sys import stdout as terminal
from time import sleep
from itertools import cycle
from threading import Thread

done = False

def animate():
    loaderString = ''
    while not done:
        for c in ['J',"A","R","V","I","S"]:
            loaderString += c
            terminal.write('\rloading ' + loaderString)
            # terminal.flush()
            sleep(0.1)
        terminal.write('Done!   ')
        terminal.flush()

t = Thread(target=animate)
t.start()
sleep(5)
done = True