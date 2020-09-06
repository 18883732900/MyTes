from random import  randint
def number():
    s = randint(0,99999999)
    top=[177,188,199,132,186,152,189]
    t=randint(0,len(top)-1)
    return f'{top[t]}{s:08d}'



