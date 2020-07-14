
'''
    A Queue is a collections of elements where the first element added will be the first element to be removed, just like in a real queue.
    We insert to the back and delete from the front.

    Use a queue when you want to get things out in the order that you put them in.

    Applications:
        - Scheduling jobs, processing, BFS

    Methods:
        - enqueue(data): Add element to the back of the queue
        - dequeue(): Remove and return the first element
        - peek(): Return the last element
        - isEmpty(): Check if stack is empty
'''

from Node import Node

class Queue():
    def __init__(self, data=None):
        self.front = Node(data) if data != None else None
        self.back = None

    def enqueue(self, data):
        if not data:
            return

        newNode = Node(data)

        if self.back:
            self.back.next = newNode

        self.back = newNode

        if self.front is None:
            self.front = newNode

    def dequeue(self):
        if not self.front:
            return None

        data = self.front.data
        self.front = self.front.next
        return data

    def peek(self):
        return self.front.data if self.front else None

    def isEmpty(self):
        return self.front == None

queue = Queue()
queue.enqueue(5)
queue.enqueue(15)
queue.enqueue(25)
print(queue.dequeue())
print(queue.peek()) # 15
print(queue.isEmpty()) # false