from stack import Stack

def divideByTwo(num):
    stack = Stack()

    while num > 0:
        reminder = num % 2
        stack.push(reminder)
        num = num // 2

    binary = ''

    while not stack.isEmpty():
        binary += str(stack.pop())

    return binary

print(divideByTwo(242))