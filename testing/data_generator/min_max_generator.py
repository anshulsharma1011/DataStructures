from DataStructures.testing.data_generator import constants

def getMinMax():
    step = constants.data_step
    start = constants.data_start
    count = constants.totalCount
    arr = []
    for i in range(0,count):
        temp_arr = []
        temp_arr.append(start)
        temp_arr.append(start+step)
        start = start+step
        arr.append(temp_arr)
    return arr

if __name__ == '__main__':
    getMinMax()