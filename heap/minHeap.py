class MinHeap:
    def __init__(self):
        self.count = 0
        self.heap_list = []

    # - insert
    def insert(self, val):
        self.heap_list.append(val)
        # could ge tthe size ith len but gonna go with count
        self.count += 1
        self.sift_up(self.count)

    # - sift_up - needed for insert
    def sift_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i], self.heap_list[i//2] = self.heap_list[i//2], self.heap_list[i]
            i = i // 2

    # - get_min - returns the min item, without removing it
    def get_min(self):
        return self.heap_list[0]

    # - get_size() - return number of elements stored
    def get_size(self):
        return self.count

    # - is_empty() - returns true if heap contains no elements
    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False

    # - extract_min - returns the min item, removing it
    def extract_min(self):
        pass

    # - sift_down - needed for extract_max
    def sift_down(self, i):


    # - remove(x) - removes item at index x
    # - heapify - create a heap from an array of elements, needed for heap_sort
    # - heap_sort() - take an unsorted array and turn it into a sorted array in -place using a max heap or min heap
print(1//2)