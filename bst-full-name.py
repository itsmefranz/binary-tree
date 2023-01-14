class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
            
        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        # this method returns a list of full_name in a specific order
        full_name = []

        # visit left tree
        if self.left:
            full_name += self.left.in_order_traversal()

        # visit base node
        full_name.append(self.data)

        # visit right tree
        if self.right:
            full_name += self.right.in_order_traversal()

        return full_name
        
    def pre_order_traversal(self):
        full_name = [self.data]
         
        # visit left tree
        if self.left:
            full_name += self.left.in_order_traversal()

        # visit right tree
        if self.right:
            full_name += self.right.in_order_traversal()

        return full_name

    def post_order_traversal(self):
        full_name = []

        # visit left subtree
        if self.left:
            full_name += self.left.post_order_traversal()
        
        # visit left subtree
        if self.right:
            full_name += self.right.post_order_traversal()

        #visit base node
        full_name.append(self.data)

        return full_name

    def search(self, val):
        if self.data == val:
            return True
        
        # it is possible that the value might be in left subtree
        if val < self.data:
            # checks if the left subtree has the value
            if self.left:
                return self.left.search(val)
            else:
                return False

        # it is possible that the value might be in right subtree
        if val > self.data:
            # checks if the left subtree has the value
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

def build_tree(full_name):
    root = BinarySearchTreeNode(full_name[0])

    for i in range(1,len(full_name)):
        root.add_child(full_name[i])

    return root

if __name__ == '__main__':