class BST:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

# - insert // insert value into tree
    def insert(self, val):
        if not self.val:
            self.val = val
            return
        if self.val == val:
            return
        if val < self.val:
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
        pass

# - print_values // prints the values in the tree, from min to max
    def print_values(self, vals):
        if self.left is not None:
            self.left.print_values(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.print_values(vals)
        return vals



# - delete_tree
    def delete_tree(self):
        pass

# - is_in_tree // returns true if given value exists in the tree
    def is_in_tree(self,val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.is_in_tree(val)
        if self.right == None:
            return False
        return self.right.is_in_tree(val)

    def counter(self, node):
        if node == None:
            return -1
        left_count = self.counter(node.left)
        right_count = self.counter(node.right)
        return max([left_count, right_count]) + 1
# - get_height // returns the height in nodes(single node 's height is 1)
#     mine return 0 when there's only one node, acceptable by me
    def get_height(self):
        return self.counter(self)

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
    def is_binary_search_tree(self, vals):

        if self.left is not None:
            if self.left.val > self.val:
                return False
            self.left.is_binary_search_tree(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            if self.right.val < self.val:
                return False
            self.right.is_binary_search_tree(vals)

        return True



# - delete_value
    def delete_value(self, val):
        if self == None: # if there's no node
            return self

        if val < self.val:
            if self.left:
                self.left = self.left.delete_value(val)
            return self

        if val > self.val:
            if self.right:
                self.right = self.right.delete_value(val)
            return self

        if self.right == None:
            return self.left

        if self.left == None:
            return self.right

        min_larger_node = self.right

        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete_value(min_larger_node.val)
        return self


    def find_value(self,val):
        if val == self.val:
            return self

        if val < self.val:
            if self.left == None:
                return False
            return self.left.find_value(val)
        if self.right == None:
            return False
        return self.right.find_value(val)

    # this one's mainly for the successor
    def find_min(self ,node):
        while node.left:
            node = node.left
        return node
# - get_successor // returns next - highest value in tree after given value, -1 if none
    def get_successor(self, val):

        # find the val if it exists, gonna use a method for that
        current = self.find_value(val)
        if current == None:
            return None
        if current.right != None:
            return self.find_min(current.right).val
        else:
            # then get the parent it doesn't have a right node
            successor = None
            ancestor = self
            while ancestor != current:
                if current.val < ancestor.val:
                    successor = ancestor
                    ancestor = ancestor.val
                else:
                    ancestor = ancestor.right
            return successor.val



if __name__ == '__main__':
    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18, 20, 2]
    bst = BST()
    for num in nums:
        bst.insert(num)

    print(bst.print_values([]))
    bst.delete_value(21)
    print(bst.print_values([]))
    print(11 ,"in tree?", bst.is_in_tree(11))
    print("sucessor of", 3, "is", bst.get_successor(3))
    print("is it a binary search tree: ",bst.is_binary_search_tree([]))
    print("tree height: ", bst.get_height())