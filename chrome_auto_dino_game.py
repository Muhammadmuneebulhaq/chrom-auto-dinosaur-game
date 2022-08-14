'''
Author: Muhammad Muneeb Ul Haq
Date started: 9 May 2022
Date completed: 15 May 2022
This code automates the Chrome dino game (working may vary at different
screen sizes)
'''

import pyautogui
from PIL import ImageGrab
import time

def is_collide(data):
    for i in range(500, 550):
        for  j in range(400, 430):
            if data[i, j] != data[400,400] :
                pyautogui.keyDown('up')        
                return 

if __name__ == "__main__":
    print('Dino game is about to start')
    time.sleep(2)
    print('And here we go...')
    print('game started')
    while True:
        #ImageGrab.grab() takes the screen shot of the screen 
        #convert('L') convert it into grey image
        #load() loads the image into the form of an array
        is_collide(ImageGrab.grab().convert('L').load())
    