import numpy as np
from PIL import ImageGrab, Image
import cv2
import pytesseract
import math
import requests
import json
import re
import time
import random
from pygame._sdl2 import get_num_audio_devices, get_audio_device_name
from pygame import mixer #Playing sound
from pynput.keyboard import Key, Controller


mlist = ['badluck.mp3', 'chair.mp3', 'headshot.mp3', 'health.mp3', 'keyboard.mp3', 'lag.mp3', 'los.mp3', 'omfg.mp3', 'ping.mp3', 'wifi.mp3', 'wtfh.mp3']
mixer.init() #Initialize the mixer, this will allow the next command to work
[get_audio_device_name(x, 0).decode() for x in range(get_num_audio_devices(0))] #Returns playback devices
mixer.quit() #Quit the mixer as it's initialized on your main playback device
mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)') #Initialize it with the correct device
 #Load the mp3
keyboard = Controller()

config = json.loads(open('config.json').read())
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
global last
last = None

def song():
    while song != last
        song = random.choice(mlist)
    last = song
    return song

def mix():
    music = song()
    mixer.music.load()
    print('inside mix')
    mixer.music.play() #Play it

    keyboard.press('v')
    while mixer.music.get_busy():
        
        time.sleep(0.4)
    
    keyboard.release('v')
    print("loop done")

    mixer.music.stop()



class Imaging:
    def __init__(self):
        self.currentHealth = 100
        self.ocrErr = False

    def process(self, greyImg):
        
        
        self.currentHealth
        txt = pytesseract.image_to_string(greyImg,lang='eng')
        list_of_numbers = re.findall(r'\d+', txt)
        txt = ''.join(list_of_numbers)
        print('txt = ' + txt)
        if not txt == '':
            print('inside if not txt')
            new_health = ''.join(filter(lambda x: x.isdigit(), txt))
            if not new_health == '':
                if new_health == '01':
                    new_health = '0'
                    print('Health: {}'.format(new_health))
                else:
                    print('Health: {}'.format(new_health))
            try:
                print('inside try')
                health = int(txt)
                self.ocrErr = False
            except:
                print('inside except')
                health = self.currentHealth
                if not self.ocrErr:
                    health = self.currentHealth - 1
                    self.ocrErr = True

            if health < self.currentHealth:
                print('self:' + str(self.currentHealth))
                print('inside health comparison')
                self.currentHealth = health
                print('self:' + str(self.currentHealth))
                return True
            if health <= 100:
                self.currentHealth = health
            
            return False

def main():
    print('in main')
    imaging = Imaging()
    while(True):
        x = config['x_cord']
        y = config['y_cord']
        offx = config['off_x']
        offy = config['off_y']
        
        new_size_x = 300
        new_size_y = 100

        img = ImageGrab.grab(bbox=(x, y, x + offx, y + offy)).convert('L')
        
        #helping with image processing
        img = np.array(img)
        cv2.imshow('Valorant Health', img)
        
        if imaging.process(img):
            if not config['raspberry_pi_host'] is None:
                print('inside if not')
            print('inside imaging')
            mix()

        if cv2.waitKey(25) & 0xFF == ord('q'):  
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()
