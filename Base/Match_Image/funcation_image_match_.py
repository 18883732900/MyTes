from pymouse import PyMouse
from pykeyboard import PyKeyboard
from Base.Match_Image.Image_match import ImageMath
import time


class Image_Test():
    def __init__(self):
        self.mouse = PyMouse()
        self.keyboard = PyKeyboard()
        self.match = ImageMath()

    # def start_server(self):
    #     # 模拟按住 左边windows徽 (复杂写法，避免忘记使用方式)
    #     self.keyboard.press_key(self.keyboard.windows_l_key)
    #     # 模拟松开windows
    #     self.keyboard.release_key(self.keyboard.windows_l_key)
    #     # 输入cmd
    #     time.sleep(1)
    #     self.keyboard.type_string('cmd')
    #     time.sleep(1.5)
    #     self.keyboard.tap_key(self.keyboard.right_key)
    #     time.sleep(1)
    #     self.keyboard.tap_key(self.keyboard.down_key)
    #     time.sleep(1)
    #     self.keyboard.tap_key(self.keyboard.enter_key)
    #     time.sleep(2)
    #     self.keyboard.type_string('net start mysql')
    #     self.keyboard.tap_key(self.keyboard.enter_key)


    def on_click(self, target, n=2):
        x, y = self.match.find_image(target)
        time.sleep(1)
        for i in range(n):
            # 右键点击
            # self.mouse.click(x, y,2)

            # 双击
            self.mouse.click(x,y)
        print('在%d，%d位置单机%d次' % (x, y, n))
        time.sleep(1)
        return x, y

    def input(self,target,text):
        x,y=self.on_click(target,n=2)
        self.keyboard.type_string(text)
        time.sleep(1)
        print('在%d，%d位置输入%d' % ( x,y,text))

    def select(self, target, count=1):
        x, y = self.on_click(target)
        for i in range(count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(0.5)
        print('在%d，%d位置选择第%s' % (x, y, count))


if __name__ == '__main__':


    c = Image_Test()
    # c.start_server()
    # c.on_click('微信截图_20200909222517.png')
