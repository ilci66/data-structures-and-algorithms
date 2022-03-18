import ctypes
# python doesn't have a static array as in java

class DynamicArray(object):
    # the constructor
    def __init__(self):
        self.n = 0 # Actual element count inside the array
        self.capacity = 1 # initial capacity
        self.A = self.make_array(self.capacity) # create the array with given capacity

    # len(instance) returns the length of the instance
    def __len__(self):
        return self.n

    def __getitem__(self, k):
        # handle the if the k index exists in the array
        if not 0 <= k < self.n:
            return IndexError('Out of bounds! No insertion')
        return self.A[k] # return if it exists of course

    def append(self, ele):
        # if the capacity is reached double the size
        # don't forget in python and java it's "=="
        if self.n == self.capacity:
            self._resize(2*self.capacity)

        self.A[self.n] = ele # append the element
        self.n += 1 # increase the size of the array by one

    def insertAt(self, item, index): # insert at a certain index
        if index < 0 or index > self.n:
            # if index is negative or larger than the array size
            print("Invalid index")
            return

        # again if the size reaches the capacity
        if self.n == self.capacity:
            self._resize(2*self.capacity)

        # range(start, stop, step), just a reminder
        # moving all the items after the given index one poing right
        # in order to create the space, going right to left
        for i in range(self.n-1, index-1, -1):
            self.A[i+1] = self.A[i]

        #finally inserting the item
        self.A[index] = item
        self.n+=1

    # delete from the end of the array
    def delete(self):
        # handle an empty array
        if self.n == 0:
            print("Array is empty")
            return

        # give 0 to the last item in the array
        self.A[self.n-1]
        self.n -= 1

    # remove at a certain index
    def removeAt(self, index):
        # similar to the insertAt method
        if self.n == 0:
            print("Array is empty")

        if index < 0 or index >= self.n:
            return IndexError("Index is out of bounds! No deletion")

        # if it's the last item in the array
        if index == self.n -1:
            self.A[index] = 0
            self.n -= 1
            return
        for i in range(index, self.n-1):
            # moving the elements one index left
            self.A[i] = self.A[i+1]

        # took out an element so shorten the array
        self.A[self.n-1] = 0
        self.n -= 1

    # Finally resize method for the capacity increases
    # Doubling the capacity each time
    def _resize(self, new_cap):

        B = self.make_array(new_cap)  # New bigger array

        # move everything inside the new value
        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()


# Instantiate
arr = DynamicArray()
# Append new element
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)
arr.append(5)
arr.append(6)
print(len(arr))