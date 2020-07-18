from stack import Stack

"""
Check if a string has equal matching parentheses. Examples:
([{}]) is correct
([{]]) is incorrect
"""
def matching_parentheses(strInput):
    stack = Stack()

    for char in strInput:

        # add opening parentheses to the stack 
        if char in '([{':
            stack.push(char)
        else:
            # found closing parentheses and stack is not empty
            if stack.isEmpty():
                return False

            top = stack.pop()
            if not isMatching(top, char):
                return False

    return True

def isMatching(opening, closing):
    return opening == '(' and closing == ')' or opening == '[' and closing == ']' or opening == '{' and closing == '}' 

print(matching_parentheses('[({[([])]})]'))