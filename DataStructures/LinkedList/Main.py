from LinkedList import LinkedList

if __name__ == "__main__":
    linkedList = LinkedList()

    if linkedList.isEmpty():
        for char in ['a','b','c','d','e','f','g','h','i','j']:
            linkedList.append(char)

    linkedList.insert(0, '0')
    linkedList.insert(2, '1')

    print(linkedList.get(4))
    print(linkedList.get(100))

    linkedList.prepend('first')
    linkedList.remove('0')

    print('length', linkedList.length())
    print('Has g?', linkedList.find('g'))

    print(linkedList.get_all())