from Node import Node

'''
    A Tree is a data structure where each node can have at most 2 children. A common type of tree is a Binary Search Tree(BST)
    In BST, every node has a value that is greater than or equal to the node values in the left sub-tree, so the left node is always less than the right node

    Traversal: Depth-first search is a type of traversal that goes deep as much as possible in every child before exploring the next sibling.
        There are several ways to perform a depth-first search: in-order, pre-order and post-order.

    A tree can also be represented using an Array, say a node is at tree[k] we can get it's left child using tree[k*2+1] and right child using tree[k*2+2]
'''

class BST():
    def __init__(self, root=None):
        self.root = root

    # Find the place where we want to add a new node in order to keep the tree sorted
    def insert(self, data):
        if not data:
            return

        self.root = self.insert_recursive(self.root, data)

    def insert_recursive(self, node, data):
        if not node:
            return Node(data)

        if data < node.data:
            node.left = self.insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self.insert_recursive(node.right, data)

        return node

    def contains(self, data):
        return self.contains_recursive(self.root, data)

    def contains_recursive(self, node, data):
        if not node:
            print('hit a base case')
            return False

        elif node.data == data:
            print('hit a base case')
            return True

        elif data < node.data:
            res = self.contains_recursive(node.left, data)
            print('backtrack', res)
            return res

        else:
            res = self.contains_recursive(node.right, data)
            print('backtrack', res)
            return res

    def delete(self, data):
        if not data:
            return False

        return self.delete_recursive(self.root, data) 

    def delete_recursive(self, node, data):
        if not node:
            return None

        if node.data == data:
            if not node.left and not node.right:
                node = None

            if not node.right:
                return node.left

            if not node.left:
                return node.right

            smallestValue = self.findSmallestValue(node.right)
            node.data = smallestValue
            node.right = self.delete_recursive(node.right, smallestValue)
            return node

        if data < node.data:
            node.left = self.delete_recursive(node.left, data)
            return node
        else:
            node.right = self.delete_recursive(node.right, data)
            return node


    def findSmallestValue(self, parent):
        return parent.data if not parent.left else self.findSmallestValue(parent.left)

    # Traversal
    def in_order_traversal(self):
        self.in_order_recursive(self.root)

    def pre_order_traversal(self):
        self.pre_order_recusrive(self.root)

    def post_order_traversal(self):
        self.post_order_recusrive(self.root)

    def in_order_recursive(self, node):
        if node:
            print(node.data)
            self.in_order_recursive(node.left)
            self.in_order_recursive(node.right)

    def pre_order_recusrive(self, node):
        if node:
            self.pre_order_recusrive(node.left)
            print(node.data)
            self.pre_order_recusrive(node.right)

    def post_order_recusrive(self, node):
        if node:
            self.post_order_recusrive(node.left)
            self.post_order_recusrive(node.right)
            print(node.data)

    def in_order_iterative(self):
        stack = [self.root]

        while stack:
            node = stack.pop()
            if node:
                print(node.data)
                stack.append(node.right)
                stack.append(node.left)


bst = BST()

bst.insert(6)
bst.insert(4)
bst.insert(8)
bst.insert(3)
bst.insert(5)
bst.insert(7)
bst.insert(9)

print('Output:', bst.contains(5))

bst.in_order_traversal()