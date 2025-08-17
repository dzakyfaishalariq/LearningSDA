# serching valeu small in arrays 
def min(arr: list)->int:
    nilai = arr[0]
    for i in arr:
        if i < nilai:
            nilai = i
    return nilai

# learning booble sorting
def booble_sorting(arr: list)->list:
    long_arr = len(arr)
    for i in range(long_arr):
        for j in range(long_arr-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f"iterasi {i} : {arr}")
    return arr

# peningkatan booble sorting
def booble_sortingV2(arr: list)->list:
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped=True
        if not swapped:
            break
        print(f"iterasi {i} : {arr}")
    return arr        

