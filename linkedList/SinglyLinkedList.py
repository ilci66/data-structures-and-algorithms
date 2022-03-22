class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node

    def isEmpty(self):
        size = 0
        temp = self.head
        while(temp):
            size += 1
            temp = temp.next
        print("is it empty: ", bool(size == 0))

    def front(self):
        return self.head.data

    def back(self):
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        return temp.data

    def get_size(self):
        size = 0
        temp = self.head
        while(temp):
            size += 1
            temp = temp.next
        print ("size is: ", size)
        return size

    # going one by one printing the values
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next

    def valueAt(self, index):
        temp = self.head
        nth = 0
        while(temp):
            if(index != nth):
                nth += 1
                temp = temp.next
            else:
                print (index,"- nth item value is: ",temp.data)
                return
    def push_front(self, value):
        toAdd = Node(value)
        temp = self.head
        self.head = toAdd
        toAdd.next = temp

    def pop_front(self):
        self.head = self.head.next

    def push_back(self, value):
        toAdd = Node(value)
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = toAdd

    def pop_back(self):
        temp = self.head
        while(temp.next.next != None):
            temp = temp.next
        print("removed: ",temp.next.data)
        temp.next = None

    def insert(self, index, value):
        toInsert = Node(value)
        temp = self.head
        nth = 0
        while(temp):
            if(nth == index):
                oldTempNext = temp.next
                toInsert.next = oldTempNext
                temp.next = toInsert

            temp = temp.next
            nth += 1

    # got a little fancy with this one
    def erase(self, index):
        if(index < 0):
            print('index can\'t be negative')
        if(index == 0):
            self.pop_front()

        nth = 1
        prev = self.head
        current = self.head.next

        while(current):
            if(index == nth):
                prev.next = current.next
                current.next = None
                return
            nth += 1
            prev = current
            current = current.next
        print("out of bounds")

    # value_n_from_end(n) - returns the value of the node at nth position from the end of the list
    # I decided to start the indexing from 0, so zeroth is the last one
    def value_n_from_end(self, index):
        nth = 1
        size = self.get_size()
        wanted = size - index
        current = self.head
        if (wanted == 0):
            print("wanted data is: ", current.data)
            return current.data
        while(current):
            if(nth == wanted):
                print("returning: ", current.data)
                return current.data

            current = current.next
            nth += 1


    # Going with the iterative way of doing this because the space complexity is O(1)
    # def reverse(self): # Iterative
    #     prev = None
    #     current = self.head
    #     while(current):
    #         next = current.next
    #         current.next = prev
    #         prev = current
    #         current = next
    #         # print("current", current.data)
    #     self.head = prev # I forgot about the head for like 10 mins
    #
    def reverse(self, node): # recursive
        if(node == None):
            return node
        if(node.next):
            return node

        node1 = self.reverse(node.next) # call recursively until we hit the base
        node.next.next = node # points to itself
        node.next = None
        return node1

if __name__ == '__main__':
    # initialize with an empty list
    s_l_list = LinkedList()

    # the first node, gotta define the head
    s_l_list.head = Node(1)

    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    # chain'em up
    s_l_list.head.next = second
    second.next = third
    third.next = fourth

    # s_l_list.printList()
    # s_l_list.get_size()
    # s_l_list.isEmpty()
    # s_l_list.valueAt(0)
    # s_l_list.valueAt(2)
    # s_l_list.push_back(5)
    # s_l_list.printList()
    # s_l_list.push_back(6)
    # s_l_list.printList()
    # s_l_list.pop_back()
    # s_l_list.printList()

    # s_l_list.push_front(0)
    # s_l_list.printList()
    # s_l_list.pop_front()
    # s_l_list.printList()
    # print(s_l_list.front())
    # print(s_l_list.back())
    #s_l_list.printList()
    #s_l_list.insert(1, 77)
    #s_l_list.printList()

    # s_l_list.erase(2)
    # s_l_list.printList()

    # s_l_list.value_n_from_end(0)
    # s_l_list.reverse() # for the iterative method
    s_l_list.reverse(s_l_list.head) # call the method with the current head
    s_l_list.printList()