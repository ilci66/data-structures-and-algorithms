def binary_search(arr, left, right, x):

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, left, mid-1, x)

        else:
            return binary_search(arr, left+1, right, x)
    else:
        return -1

arr = [2,3,4,5,6,8,11]
x = 7
x2 = 8
r = binary_search(arr, 0, len(arr)-1, x)
r2 = binary_search(arr, 0, len(arr)-1, x2)
print("r => ", r)
print("r2 => ", r2)