import xlrd


class read_xlsx():
    def read_xls(self,filename):
        workbook = xlrd.open_workbook(filename)
        sheel = workbook.sheet_by_index(0)
        col = int(sheel.ncols)
        row = sheel.nrows
        print(row, col)
        key = sheel.row_values(0)
        print(key)
        list = []
        for i in range(1, row):
            value = sheel.row_values(i)
            dic2 = {}
            for p in range(col):
                dic2[key[p]] = value[p]
            list.append(dic2)
        print(list)

