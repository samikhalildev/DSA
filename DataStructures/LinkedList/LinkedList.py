
'''
    A LinkedList contains a collection of nodes, each node contains a value and a pointer to the next element.
    a -> b -> c -> d

    Why is it good: 
        - Unlike array, we don't set the size of how many elements we want
        - Insertion and deletion is faster than an Array, constant time.

    Why is it bad:
        - Slow look up O(n). We can't index the list like we would do in an Array.

    Methods:
        - get(index): Return the value stored at a given index/position
        - insert(index, data): Add node to a specific index
        - append(data): Append node to the end of the list
        - prepend(data): Add node to the beginning of the list
        - remove(data): Remove the first node that is found
        - isEmpty(): Check if list is empty
        - length(): Return the number of nodes in the list
        - get_all(): Return all node values in the list
        - find(data): Return true if data is in the list
'''
from Node import Node

class LinkedList():
    def __init__(self, data=None):
        self.head = Node(data) if data != None else None

    def get(self, index):
        if self.head == None or index < 0:
            return -1

        curr = self.head

        for i in range(index + 1):
            if i == index:
                return curr.data

            if curr.next:
                curr = curr.next
                i += 1
            else:
                return -1
        return -1

    def insert(self, index, data):
        if data == None or index < 0:
            return

        curr = self.head
        newNode = Node(data)

        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return

        previous = curr
        i = 0 

        while curr:
            if i == index:
                previous.next = newNode
                newNode.next = curr
                return 

            previous = curr
            curr = curr.next
            i += 1

        if index == i:
            previous.next = Node(data)

    def append(self, data):
        if not data: 
            return

        curr = self.head

        # case where head is empty, set node as the head
        if not curr:
            self.head = Node(data)
            return

        while curr.next:
            curr = curr.next

        curr.next = Node(data)

    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def remove(self, data):
        if not data:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        curr = self.head
        previous = curr

        while curr:
            if curr.data == data:
                previous.next = curr.next if curr.next else None
                return

            previous = curr
            curr = curr.next

        return

    def find(self, data):
        if not data:
            return False

        curr = self.head
  
        while curr:
            if curr.data == data:
                return True

            curr = curr.next

        return False

    def get_all(self):
        curr = self.head
        output = ''

        while curr:
            output += str(curr.data)
            if curr.next:
                output += ' -> '
            curr = curr.next

        return output
    
    def isEmpty(self):
        return self.head is None

    def length(self):
        curr = self.head
        length = 0

        while curr:
            length += 1
            curr = curr.next

        return length

    def length_recursive(self, node):
        if node is None:
            return 0

        return 1 + self.length_recursive(node.next)
