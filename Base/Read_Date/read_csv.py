import csv


class Readcsv():
    def read_csv(self, filname, Start_index=0, End_index=None, cut=None):
        csv_read = csv.reader(open(filname))
        my_list = []
        for i in csv_read:
            my_list.append(i)
        lise = my_list[Start_index:End_index:cut]
        return lise


if __name__ == '__main__':
    cs = Readcsv()
    print(cs.read_csv())
