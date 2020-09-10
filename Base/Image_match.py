from PIL import Image, ImageGrab
import os


class ImageMath:
    def __init__(self):
        self.screen = None
        self.template = None
        self.screen_data = None
        self.template_data = None

    def compare(self, p1, p2):
        return p1[0] == p2[0] and p1[1] == p2[1] and p1[2] == p2[2] and p1[3] == p2[3]

    def find_image(self, target):
        # 日常测试使用
        file_path = os.path.join(r'C:\Users\26765\Desktop\python测试\Ui自动化', 'Template_Image')
        # jenkins使用
        # file_path = os.path.join(os.getcwd(), 'Template_Image')

        self.screen = ImageGrab.grab().convert("RGBA")

        self.template = Image.open(os.path.join(file_path, target)).convert("RGBA")

        screen_width, screen_height = self.screen.size

        template_width, template_height = self.template.size

        self.screen_data = self.screen.load()

        self.template_data = self.template.load()

        pos_x = -1
        pos_y = -1

        for y in range(screen_height - template_height):

            for x in range(screen_width - template_width):

                if self.compare(self.screen_data[x, y], self.template_data[0, 0]) \
                        and self.compare(self.screen_data[x + template_width - 1, y],
                                         self.template_data[template_width - 1, 0]) \
                        and self.compare(self.screen_data[x + template_width - 1, y + template_height - 1],
                                         self.template_data[template_width - 1, template_height - 1]) \
                        and self.compare(self.screen_data[x, y + template_height - 1],
                                         self.template_data[0, template_height - 1]) \
                        and self.compare(self.screen_data[x + template_width / 2, y + template_height / 2],
                                         self.template_data[template_width / 2, template_height / 2]):
                        is_math = self.check_match_smil(x, y)
                        if is_math:
                            pos_x = x + template_width / 2
                            pos_y = y + template_height / 2
                            return  int(pos_x) ,int(pos_y)
        return pos_x, pos_y


    def check_match(self,x,y):
        template_width,template_height = self.template.size
        for smll_y in range(template_height):
            for smll_x in range(template_width):
                if not self.compare(self.screen_data[x+smll_x,y+smll_y],self.template_data[smll_x,smll_y]):
                    return False
        return True


    def check_match_smil(self,x,y,similarity=1):
        template_width,template_height = self.template.size
        total_count=template_height*template_width
        unmatch_count=0
        for smll_y in range(template_height):
            for smll_x in range(template_width):
                if not self.compare(self.screen_data[x+smll_x,y+smll_y],self.template_data[smll_x,smll_y]):
                    unmatch_count +=1

        return  unmatch_count/total_count <= 1-similarity



    def check_exist(self,target):
        x,y=self.find_image(target)
        return x != -1 and y != -1








if __name__ == '__main__':
    s='微信截图_20200910004532.png'
    x,y=ImageMath().find_image(s)
    print(x)
    print(y)

    print(ImageMath().check_exist(s))
