import random


def name():
    firstname = ['周', '王', '张', '杨', '陈']
    tailname = ['大', '二', '三', '四', '五']
    name = f'{firstname[random.randint(0, len(firstname) - 1)]}{tailname[random.randint(0, len(tailname) - 1)]}'
    return name
