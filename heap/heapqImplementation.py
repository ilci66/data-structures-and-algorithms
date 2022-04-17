from heapq import heapify, heappush, heappop
# apparently if creates a min heap by default

heap = []
heapify(heap)

heappush(heap, 10)
heappush(heap, 30)
heappush(heap, 20)
heappush(heap, 400)

# printing the value of minimum element
print("Head value of heap : " + str(heap[0]))

# printing the elements of the heap
print("The heap elements : ")
for i in heap:
    print(i, end='-')
print("\n")

element = heappop(heap)
print("After the pop : ")

for i in heap:
    print(i, end='-')
# printing the elements of the heap
