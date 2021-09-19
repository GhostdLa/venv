
import time
import requests
import typing
import pyautogui

LOVE = "A lot of what are events?"

class Falling:
    def __init__(self, LOVE):
        self.LOVE = LOVE

    def show(self):
       	n = 0
        while n < 3600:
        	print(self.LOVE, n)
        	time.sleep(1)
        	n = n + 1

    def tyme(self):
    	typing.AsyncGenerator(self: --> None)


bar = Falling('data')
bar.show()