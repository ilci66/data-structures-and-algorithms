# Implement with array using linear probing,
class HashLinearProbing:
    def __init__(self):
        self.max = 8
        self.arr = [[] for i in range(self.max)]

# - hash(k, m) - m is size of hash table
#     instead of giving the size like this
#     I'm using the max size I defined for my
#     array in the constructor
    def get_hash(self, k):
        hash = 0
        for c in k:
            hash += ord(c)
        return hash % self.max

# - add(key, value) - if key already exists, update value
    def __setitem__(self, key, value): # Set the value of a at index b to c
        h = self.get_hash(key)
        self.arr[h].append({ key: value })

# - exists(key)
    def exists(self, key):
        h = self.get_hash(key)

# - get(key)
    def __getitem__(self, key):
        h = self.get_hash(key)
        print("fget item", self.arr[h])
        for k, v in self.arr[h]:
            print("ye")
            # print(k,v)
        # if (self.exists(key)):


# - remove(key)

if __name__ == '__main__':
    h_l_p = HashLinearProbing()
    h_l_p.__setitem__("cats", 55)
    h_l_p.__setitem__("dogs", 12)
    print("asddda", h_l_p.__getitem__("cats"))
    print("asd", h_l_p.arr)