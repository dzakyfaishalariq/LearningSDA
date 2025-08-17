# serching valeu small in arrays 
def min(arr: list)->int:
    nilai = arr[0]
    for i in arr:
        if i < nilai:
            nilai = i
    return nilai
