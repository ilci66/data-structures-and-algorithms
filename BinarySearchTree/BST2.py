class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, node):
        current = self.root

        if current == None:
            self.root = node
            self.count += 1
            return
        while current:
            if current.val < node.val:
                if current.right == None:
                    current.right = node
                    self.count += 1
                    return
                current = current.right
            elif current.val > node.val:
                if current.left == None:
                    current.left = node
                    self.count += 1
                    return
                current = current.left

    def delete_value(self, val):
        current = self.root
        while current:
            if current.val > val:
                current = current.left
            if current.val < val:
                current = current.right
            if current.val == val:
                if current.left and current.right == None:
                    current.val = val
                    current.left = current.left.left
                    self.count -= 1
                    return
                elif current.left == None and current.right:
                    current.val = val
                    current.right = current.right.right
                    self.count -= 1
                    return
                elif current.left == None and current.right == None:
                    current.val = None
                    self.count -= 1
                    return
                elif current.left and current.right: # get the lowest in the right or highest in the left
                    print(current.left.val,"<--left, right-->", current.right.val)
                    change = current
                    current = current.left
                    while current:
                        current = current.right
                    print(change.val)
                    print(current.val)

    def get_count(self):
        return self.count

    def get_min(self):
        current = self.root
        if current.val == None:
            print("no item in the tree yet")
            return
        while current:
            if current.left != None:
                current = current.left
            elif current.left == None:
                return current.val

    def get_max(self):
        current = self.root
        if current.val == None:
            print("no item in the tree yet")
            return
        while current:
            if current.right != None:
                current = current.right
            elif current.right == None:
                return current.val


    def print_values(self, node): # prints the values in the tree, from min to max, so inorder traversal logic
        if node.left != None:
            self.print_values(node.left)
        if(node.val != None):
            print(node.val)
        if node.right != None:
            self.print_values(node.right)

if __name__ == '__main__':
    d = Node(40)
    a = Node(20)
    b = Node(10)
    c = Node(30)
    e = Node(70)
    f = Node(60)
    g = Node(50)
    h = Node(80)

    b_s_t = BinarySearchTree()

    b_s_t.insert(d)
    b_s_t.insert(a)
    b_s_t.insert(b)
    b_s_t.insert(c)
    b_s_t.insert(e)
    b_s_t.insert(f)
    b_s_t.insert(g)
    b_s_t.insert(h)

    # print(b_s_t.root.val)
    # print("right, left", b_s_t.root.right.left.val)
    # print("left left ",b_s_t.root.left.left.val)
    # print("right right ",b_s_t.root.right.right.val)

    print("min: ",b_s_t.get_min())
    print("min: ",b_s_t.get_max())

    b_s_t.print_values(b_s_t.root)
    b_s_t.delete_value(70)
    print("after the deletion")
    b_s_t.print_values(b_s_t.root)

    print("node count is: ",b_s_t.get_count())