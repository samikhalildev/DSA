
'''
    a -> b -> c -> d
    Methods: Append, Insert, Remove, length
'''
from Node import Node

class LinkedList():
    def __init__(self, head):
        self.head = head

node = Node('a')
print(node.val)