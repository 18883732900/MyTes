from pymouse import  PyMouse
from pykeyboard import PyKeyboard
from Base.Image_match import ImageMath
import os
import time

class Image_Test():
    def __init__(self):
        self.mouse=PyMouse()
        self.keyboard=PyKeyboard()
        self.match=ImageMath()

    def start_app(self):
        pass

    def on_click(self,target,n=1):
        x,y=ImageMath().find_image(target)
        self.mouse.click(x,y,n=n)
        print('在%d，%d位置单机%d次' % ( x,y,n ))
        return x,y

    def input(self,target,text):
        x,y=self.on_click(target,n=2)
        self.keyboard.type_string(text)
        print('在%d，%d位置输入%d' % ( x,y,text))


    def select(self,target,count=1):
        x,y=self.on_click(target)
        for i in range(count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(0.5)
        print('在%d，%d位置选择第%s' % ( x,y,count))




