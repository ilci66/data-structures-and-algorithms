# Implement using linked-list, with tail pointer
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def enqueue(self, value):
        if self.tail is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def dequeue(self):
        if self.head is None:
            return None
        else:
            new_head = self.head.data
            self.head = self.head.next
            return new_head

    def isEmpty(self):
        size = 0
        temp = self.head
        while(temp):
            size += 1
            temp = temp.next
        print("is it empty: ", bool(size == 0))


    def printList(self):
        temp = self.head

        while(temp):
            print (temp.data)
            temp = temp.next



if __name__ == '__main__':

    q_s_l_l = QueueSinglyLinkedList()
    # q_s_l_l.head = Node(1)
    q_s_l_l.enqueue(2)
    q_s_l_l.enqueue(3)
    q_s_l_l.enqueue(4)
    q_s_l_l.dequeue()
    q_s_l_l.dequeue()
    q_s_l_l.dequeue()
    q_s_l_l.printList()
    q_s_l_l.isEmpty()