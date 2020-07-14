
'''
    A Stack contains elements where data is added on top and removed from top, first in, first out.

    When to use:
        - When you want to get the previous element that you put in.
        - The most recently added will be the first to be removed, like a stack of dishes
        - Get things out in the reverse order than you put them in.

    Can be implementing using an Array of LinkedList.

    Applications:
        - Backtracking algorithms such as pathfinding and traversals.
        - Compliers, parsers, expression evaluation

    Methods:
        - Push(data): Add element to the end of the stack
        - Pop(): Remove and return the last element
        - Peek(): Return the last element
        - isEmpty(): Check if stack is empty
'''

from Node import Node

class Stack():
    def __init__(self, data=None):
        self.top = Node(data) if data != None else None

    def push(self, data):
        if not data:
            return

        newNode = Node(data)

        newNode.next = self.top
        self.top = newNode

    def pop(self):
        if self.top:
            top = self.top
            self.top = self.top.next
            return top.data

    def peek(self):
        if self.top:
            return self.top.data

    def isEmpty(self):
        return self.top == None


stack = Stack()
stack.push(5)
stack.push(4)
stack.push(2)
stack.pop()
stack.pop()

print(stack.peek())