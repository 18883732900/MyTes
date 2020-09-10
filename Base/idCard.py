
import Base
from random import  randint
s=randint(0,500)
class IdNumber(object):
    __instance=None
    def __new__(cls, *args, **kwargs):
        if  cls.__instance is None:
           cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, id_number):
        # super(IdNumber, self).__init__()
        self.id = id_number

    def __str__(self):
          return Base.addrsy


        # return funcation.addrsy
    def get_check_digit(self):
        """通过身份证号获取校验码"""
        check_sum = 0
        for i in range(0, 17):
            check_sum += ((1 << (17 - i)) % 11) * int(self.id[i])
        check_digit = (12 - (check_sum % 11)) % 11
        # try:
        return check_digit if check_digit < 10 else "X"
        # except:
            # print('校验失败  身份证错误')

    @classmethod
    def generate_myid(cls, addr="浙江省", birth_day='19980807'):
        area_codes = cls(object).__str__()
        area_code = area_codes[addr]
        generate_ids = []
        '''
        随机生成一个区域码(6位数)
        area_code = "412826"
        限定出生日期范围(8位数)
        birth_day = "19610420"
        '''
        # 顺序码(2位数)
        # cls.num=0
        for i in range(100):
            sort_no = f"{i:02d}"
            for j in [x for x in range(10) if x % 2 != 0]:
                sex = j
                prefix = f"{area_code}{birth_day}{sort_no}{sex}"
                valid_bit = str(cls(prefix).get_check_digit())

                generate_ids.append(f"{prefix}{valid_bit}")
                # generate_ids.append("%d：%s%s" % (num,prefix,valid_bit))
                # cls.num +=1
        # print(num)
        return generate_ids[s]
    # def __del__(self):
    #     print(self.num)







if __name__ == "__main__":
    # generate_ids = IdNumber.generate_myid()
    # print(generate_ids)
    # for id in generate_ids:
    #     print(id)
    v='12345619440404041'
    a=IdNumber(v)
    print(len(v))
    print(a.get_check_digit())