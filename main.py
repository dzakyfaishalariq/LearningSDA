import time
from projek.recursif import *
from projek.arrays import *

if __name__ == "__main__":
    # fibonaciByForLoop(5)
    # fibonaciByRecursif(1,0)
    # data = [F(i) for i in range(20)]
    # print(data)

    # print(min([9, 39, 10, 3, 4, 1, 3, 4, -1]))
    # start_time1 = time.time()
    # print(booble_sorting([3,1,4,2,4,6,7,4,2,9]))
    # end_time1 = time.time()
    # print("result eksekusi pogram 1 : " + str(end_time1-start_time1))
    
    # start_time2 = time.time()
    # print(booble_sortingV2([3,1,4,2,4,6,7,4,2,9]))
    # end_time2 = time.time()
    # print("result eksekusi pogram 2 : " + str(end_time2-start_time2))
    
    star_time = time.time()
    arry = selection_shorting([4,2,1,20,19,22,6,9])
    print(arry)
    end_time = time.time()
    print(f"execution pogram : {end_time-star_time}")
    

    star_time1 = time.time()
    arry1 = efisiensi_selection_shotrting([4,2,1,20,19,22,6,9])
    print(arry1)
    end_time1 = time.time()
    print(f"execution pogram : {end_time1-star_time1}")