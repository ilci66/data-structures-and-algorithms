class BST:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None
        self.count = 0

# - insert // insert value into tree
    def insert(self,val):
        if not self.val: # if there's no value set it
            self.val = val
            return
        if self.val == val:  # no duplicate
            return
        if self.val > val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BST(val)
            return
        if self.right:
            self.right.insert(val)
            return
        self.right = BST(val)

# - get_node_count // get count values stored
    def get_node_count(self):


        return self.count

# - print_values // prints the values in the tree, from min to max
    def print_values(self):
        pass



# - delete_tree
    def delete_tree(self):
        pass
# - is_in_tree // returns true if given value exists in the tree
# - get_height // returns the height in nodes(single node 's height is 1)
# - get_min // returns the minimum value stored in the tree
    def get_min(self):
        current = self
        while current.left != None:
            current = current.left
        return current.val

# - get_max // returns the maximum value stored in the tree
    def get_max(self):
        current = self
        while current.right != None:
            current = current.right
        return current.val

# - is_binary_search_tree
# - delete_value
# - get_successor // returns next - highest value in tree after given value, -1 if none

if __name__ == '__main__':
    b_s_t = BST()
    b_s_t.insert(20)
    b_s_t.insert(15)
    b_s_t.insert(10)
    b_s_t.insert(5)
    b_s_t.insert(25)
    b_s_t.insert(35)
    b_s_t.insert(30)

    b_s_t.print_values()
    print("count: ",b_s_t.get_node_count())
    print("max: ",b_s_t.get_max())
    print("min: ",b_s_t.get_min())