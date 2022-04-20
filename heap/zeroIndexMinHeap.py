import sys

class ZeroIndexMinHeap:
    def __init__(self):
        self.count = 0
        self.heap_list = []

    # insert
    def insert(self, val):
        self.heap_list.append(val)
        self.count += 1
        self.sift_up(len(self.heap_list)-1)

    # sift_up
    def sift_up(self, i):
        while i+1//2 > 0:
            if self.heap_list[i] < self.heap_list[(i-1)//2]:
                self.heap_list[i], self.heap_list[(i-1)//2] = self.heap_list[(i-1)//2], self.heap_list[i]
            i = i // 2

    # get_min
    def get_min(self):
        return self.heap_list[0]

    # get_size()
    def get_size(self):
        return self.count

    # is_empty()
    def is_empty(self):
        return self.count == 0

    # extract_min
    def extract_min(self):
        self.heap_list[0] = self.heap_list[len(self.heap_list) -1]
        self.heap_list.pop()
        self.sift_down(0)

    # sift_down
    def sift_down(self, i):
        while i*2 <= self.count:
            # gonna swap with the minimum child
            m = self.min_child(i)
            if self.heap_list[i] > self.heap_list[m]:
                self.heap_list[i], self.heap_list[m] = self.heap_list[m], self.heap_list[i]
            i = m

    def min_child(self, i):
        if (i*2)+1 >  self.count:
            return i*2
        else:
            if self.heap_list[(2*i) +1] > self.heap_list[(i*2) + 2]:
                print("parent: ", self.heap_list[i],"left: ", self.heap_list[(2*i) +1], "right: ",self.heap_list[(i*2) + 2])
                return (2 * i) + 2
            else:
                return 2 * i +1

    # remove(x)
    def remove(self, val):
        i = self.find_val(val)
        self.heap_list[i] = self.heap_list[len(self.heap_list)-1]
        self.heap_list.pop()
        self.count -= 1
        self.sift_up(i)
        self.sift_down(i)

    def find_val(self, val):
        for x in range(len(self.heap_list)):
            if(self.heap_list[x] == val):
                return x

    # - heapify - create a heap from an array of elements, needed for heap_sort
    def heapify(self, arr, n, i):
        min = i
        l = (2*i) + 1
        r = (2*i) + 2

        if l < n and arr[min] > arr[l]:
            min = l

        if r < n and arr[min] > arr[r]:
            min = r

        if min != i:
            arr[i], arr[min] = arr[min], arr[i]

            self.heapify(arr, n, min)

    # - heap_sort() - take an unsorted array and turn it into a sorted array in -place using a max heap or min heap
    def heap_sort(self, arr):
        n = len(arr)

        for i in range(n//2 -1, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)

    def get_list(self):
        return self.heap_list

if __name__ == '__main__':
    # m_h = ZeroIndexMinHeap()
    # m_h.insert(5)
    # m_h.insert(1)
    # m_h.insert(6)
    # m_h.insert(2)
    # m_h.insert(4)
    # m_h.insert(8)
    # m_h.insert(3)
    # # print("heap: ", m_h.get_list())
    # # m_h.extract_min()
    # # print("heap: ", m_h.get_list())
    # m_h.remove(2)
    # print("heap: ", m_h.get_list())

    arr = [12, 11, 13, 3, 5, 7, 6]
    m_h2 = ZeroIndexMinHeap()
    m_h2.heap_sort(arr)
    for x in range(len(arr)):
        print("%d" % arr[x]),