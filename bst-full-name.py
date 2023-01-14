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

    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False


def build_tree(full_name):
    root = BinarySearchTreeNode(full_name[0])

    for i in range(1,len(full_name)):
        root.add_child(full_name[i])

    return root

if __name__ == '__main__':