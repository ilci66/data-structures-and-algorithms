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

    def getSize(self):
        size = 0
        temp = self.head
        while(temp):
            size += 1
            temp = temp.next
        print ("size is: ", size)

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
        # temp = self.head
        # nth = 0
        # while(temp):
        #     if(nth == index):



if __name__ == '__main__':
    # initialize with an empty list
    s_l_list = LinkedList()

    # the first node
    s_l_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    s_l_list.head.next = second
    second.next = third
    third.next = fourth

    # s_l_list.printList()
    # s_l_list.getSize()
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