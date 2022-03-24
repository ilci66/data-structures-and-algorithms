# Implement using fixed-sized array:
class FixedSizedArray:
    def __init__(self, capacity):
        self.my_queue = []
        self.capacity = capacity
        self.len = len(capacity)

    # enqueue(value) - adds item at end of available storage
    def enqueue(self, value):
        if(len == self.capacity):
            print("go on tomorrow, got tired")

#         - dequeue() - returns value and removes least recently added element
#         - empty()
#         - full()
