
'''
    Resursive is a method that calls it self.
    Steps:
        1. Write an base case to prevent infinite loops:
            - This will stop from calling the function. Figure out when the recusive calls should stop.
            - Only we finally return, there will be no more function calls.

        2. Handle the simplest case:
            - Do whatever you need to do, e.g. if a value matches a certain value then return true
        
        3. Write the recursive calls:
            - Call the function by passing in a different set of inputs, you may need to return or update a property
            - any code after the function call will only be executed once we reach the base case and go back to the call stack

        4. Does it work?

    Used in: print or find all elements problems, sorting algorithms, worknig with files and directories, parsing html/json files.
    Recusion can also be done iteratively using a stack and a while loop.

'''

arr = [1,[11,42,[8, 1], 4, [22,21]]]

def getSum_recusive(arr):
    results = 0

    for n in arr:
        if type(n) is list:
            results += getSum(n)
        else:
            results += n

    return results

def getSum_iterative(arr):
    results = 0
    stack = [arr]

    while stack:
        ar = stack.pop()

        for n in ar:
            if type(n) is list:
                stack.append(n)
            else:
                results += n

    return results

print(getSum_iterative(arr))


def countDown(n):
    if n <= 0:
        return
        
    print(n)
    countDown(n-1)

# countDown(9)


def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

# print(fib(9))
    