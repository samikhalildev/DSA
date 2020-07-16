
'''
    A HashTable stores a collection of key value pairs.

    When to use:
        - When you want to associate a value with a key
        - When you want fast look up and search O(1) 

    Methods:
        - setItem(key, value): Add the key value pair into the table
        - getItem(key): Return the value assoicated with the key
        - hash(key): Return an index from a given key
        - remove(key): Remove element by key if found
        - clear(): Empty the table
        - items(): Return the items in the table
        - keys(): Return the keys in the table
        - values(): Return the values in the table
'''

class HashTable:
    def __init__(self):
        self.table = [[]]

    def setItem(self, key, value):
        index = self.hash(key)
        if self.table[index]:
            self.table[index].append([key, value])
        else:
            self.table[index] = [[key, value]]

    def getItem(self, key):
        index = self.hash(key)

        if self.table[index]:
            innerList = self.table[index]
            for pair in innerList:
                if pair[0] == key:
                    return pair[1]

        return None

    def hash(self, key):
        hash = 27

        for c in key:
            hash = (39 * hash * ord(c)) % len(self.table)

        return hash

    def remove(self, key):
        index = self.hash(key)

        if self.table[index]:
            innerList = self.table[index]
            for i, pair in enumerate(innerList):
                if pair[0] == key:
                    self.table[index].pop(i)
                    return True

        return False

    def clear(self):
        self.table = [[]]

    def items(self):
        return self.table

    def keys(self):
        keys = []

        for innerList in self.table:
            try:
                keys.append(innerList[0])
            except:
                continue

        return keys

    def values(self):
        values = []

        for innerList in self.table:
            try:
                values.append(innerList[1])
            except:
                continue

        return values

hashTable = HashTable()

hashTable.setItem('name', 'Sami')
hashTable.setItem('age', 100)

print(hashTable.getItem('name'))
print(hashTable.getItem('age'))

print(hashTable.remove('age'))

print(hashTable.items())
print(hashTable.keys())

