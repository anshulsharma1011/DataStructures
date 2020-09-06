import sys
import random
from DataStructures.testing.data_generator import min_max_generator
from datetime import datetime
from DataStructures.testing.data_generator import constants

min_max_arr = min_max_generator.getMinMax()


def main():
    print(datetime.now())
    for min_max in min_max_arr:
        min_value = min_max[0]
        max_value = min_max[1]
        file = open(constants.data_basePath+str(min_value)+"_"+str(max_value)+".txt", "a")
        log = open(constants.log_basePath+str(min_value)+"_"+str(max_value)+".txt", "a")
        for i in range(min_value,max_value):
            try:
                file.write(str(random.randint(min_value,max_value))+",")
                file.write("\n")
            except Exception as e:
                log.write("Error for: "+ str(i))
        file.close()
        log.close()
    print(datetime.now())

if __name__ == '__main__':
    main()