def insertionsort(arr, size):
    for i in range(1, size):
        j = i-1
        while j>=0 and arr[i] < arr[j]:
            arr[j], arr[i] = arr[i], arr[j]
            j -= 1
            i -= 1

array = [5,4,6,8,2,7,1]
sz = len(array)
insertionsort(array, sz)
print(array)