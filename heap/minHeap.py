class MinHeap:
    def __init__(self):
        self.count = 0
        self.heap_list = []

    # - insert
    def insert(self, val):
        self.heap_list.append(val)
        # could ge the size ith len but gonna go with count
        self.count += 1
        self.sift_up(self.count-1)

    # - sift_up - needed for insert
    def sift_up(self, i):
        # This is a faulty logic which skips over the second item in the list
        # Gonna think of something else

        while i == 1 or i // 2 > 0:
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
        self.heap_list[0], self.heap_list[self.count -1] = self.heap_list[self.count -1], self.heap_list[0]
        # self.heap_list[(self.count)-1] = None
        self.heap_list.pop()
        self.count-=1
        self.sift_down(1)

    # - sift_down - needed for extract_max
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
            if self.heap_list[2*i] > self.heap_list[(i*2) +1]:
                print("parent: ", self.heap_list[1],"left: ", self.heap_list[2*i], "right: ",self.heap_list[(i*2) +1])
                return(2 * i)+1
            else:
                return 2 * i

    # - remove(x) - removes item at index x
    def remove(self, val):
        pass
    # - heapify - create a heap from an array of elements, needed for heap_sort
    # - heap_sort() - take an unsorted array and turn it into a sorted array in -place using a max heap or min heap
    def get_list(self):
        return self.heap_list

if __name__ == '__main__':
    m_h = MinHeap()
    m_h.insert(5)
    m_h.insert(1)
    m_h.insert(6)
    m_h.insert(2)
    m_h.insert(4)
    m_h.insert(8)
    m_h.insert(3)

    # print("count is: ", m_h.count)
    # print(m_h.get_list())
    m_h.extract_min()
    print(m_h.get_list())

