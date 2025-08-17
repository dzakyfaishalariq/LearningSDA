import time
from projek.recursif import *
from projek.arrays import *

if __name__ == "__main__":
    # fibonaciByForLoop(5)
    # fibonaciByRecursif(1,0)
    # data = [F(i) for i in range(20)]
    # print(data)

    # print(min([9, 39, 10, 3, 4, 1, 3, 4, -1]))
    start_time1 = time.time()
    print(booble_sorting([3,1,4,2,4,6,7,4,2,9]))
    end_time1 = time.time()
    print("result eksekusi pogram 1 : " + str(end_time1-start_time1))
    
    start_time2 = time.time()
    print(booble_sortingV2([3,1,4,2,4,6,7,4,2,9]))
    end_time2 = time.time()
    print("result eksekusi pogram 2 : " + str(end_time2-start_time2))
    
    