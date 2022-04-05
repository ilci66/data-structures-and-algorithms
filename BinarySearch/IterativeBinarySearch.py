def binary_search(arr, x):
    left = 0
    right = len(arr)-1
    mid = 0

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < x:
            left = mid + 1

        elif arr[mid] > x:
            right = mid - 1

        else:
            # return the index
            return mid

    return -1 # or return false False

arr = [ 2, 3, 4, 10, 40 ]
x = 10
x2 = 7
r = binary_search(arr, x2)
print("r =>", r)