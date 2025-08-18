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

# selection sort algorithem 
def selection_shorting(arr: list)->list:
    n = len(arr) # tentukan panjang lisnya adalah 8
    for i in range(n): # lakukan perulangan dari index 0 pada array dengan rentan 8-1 = 7 
        index_min = i # jadikan index min adalah nilai i = 0
        for j in range(i + 1, n): # lakukan perulangan j = 1 pada array dengan rentang (1,8)
            if arr[j] < arr[index_min]: # lakukan pengecekan secara berkala dari array[1] lebih kecil dari array[0]
                index_min=j # ubah nilai index_minimum menjadi nilai j = 1
        value_min = arr.pop(index_min) # ambil nilai minimum terakhir dengan menghapus nilai lis sebelumnya pada index_min yang berubah
        arr.insert(i, value_min)
    return arr

def efisiensi_selection_shotrting(arr: list)->list:
    n = len(arr)
    for i in range(n):
        index_min = i
        for j in range(i+1, n):
            if arr[j] < arr[index_min]:
                index_min = j
        arr[i], arr[index_min] = arr[index_min], arr[i]
    return arr

