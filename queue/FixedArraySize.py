# Implement using fixed-sized array:
class FixedSizedArray:
    def __init__(self, capacity):
        self.my_queue = [None] * capacity
        self.capacity = capacity
        self.len = 0
        self.head = None
        self.tail = None

    # enqueue(value) - adds item at end of available storage
    def enqueue(self, value):
        if(self.full()):
            print("It be full mon")
            return
        self.my_queue[self.len] = value
        if(self.tail == None):
            self.tail = value
            self.head = value
            self.increment_size()
        else:
            self.tail = value
            self.increment_size()

    def increment_size(self):
        self.len += 1

    # dequeue() - returns value and removes least recently added element
    def dequeue(self):
        if(self.empty()):
            print("it's empty bro")
            return
        new_arr = [None] * self.capacity
        for x in range(self.len - 1):
            print("length is: ",self.len,"x is: ", x)
            new_arr[x] = self.my_queue[x+1]
        self.my_queue = new_arr

    def decrement_size(self):
        self.len -= 1
    # empty()
    def empty(self):
        return bool(self.len == 0)
    # full()
    def full(self):
        print(bool(self.len == self.capacity))
        return bool(self.len == self.capacity)

    def printList(self):
        for x in self.my_queue:
            print("item is: ", x)

if __name__ == '__main__':
    f_s_a = FixedSizedArray(4)

    f_s_a.enqueue(1)
    f_s_a.enqueue(2)
    f_s_a.enqueue(3)
    f_s_a.enqueue(4)
    f_s_a.enqueue(5) # not supposed to add this one
    # f_s_a.printList()
    # print("is it full", f_s_a.empty())
    # print("is it empty", f_s_a.full())
    f_s_a.dequeue()
    f_s_a.printList()