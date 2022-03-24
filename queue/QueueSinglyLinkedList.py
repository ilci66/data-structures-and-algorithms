# Implement using linked-list, with tail pointer
class Node:
    def __init__(self, data):
        self.data = data
        self.next = next

class QueueSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # enqueue(value) - adds value at position at tail
    def enqueue(self, value):
        value = Node(value)
        if(self.head == None):
            self.head = value
        self.tail = value


    # dequeue() - returns value and removes least recently added element (front)
    # empty()
    def printList(self):
        print("supposed to start")
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next



# QueueSinglyLinkedList.head = Node(1)
q_s_l_l = QueueSinglyLinkedList()
first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(3)

q_s_l_l.enqueue(1)
# QueueSinglyLinkedList.tail = Node(6)

q_s_l_l.printList()