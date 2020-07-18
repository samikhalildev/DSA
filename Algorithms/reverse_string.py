from stack import Stack

def reverseString(input_string):
    stack = Stack()
    for char in input_string:
        stack.push(char)

    output = ''

    while not stack.isEmpty():
        output += str(stack.pop())

    print(output)

reverseString('Reverse Me')