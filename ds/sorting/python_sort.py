from ds import file3
from ds.sorting import constants
from ds.sorting import utils
from datetime import datetime

def sortData():
    data = file3.arr
    print(data)
    print(datetime.now())
    data.sort()
    print(datetime.now())
    file = open(constants.data_basePath+"output.txt", "a")
    # file.write(str(data))
    utils.printFormattedData(file,data)
    file.close()

if __name__ == '__main__':
    sortData()