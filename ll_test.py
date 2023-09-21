import linked_lists as ll

myList = ll.LinkedList(3)
print(myList.is_empty())
myList.append(2)
myList.append(3)
myList.prepend(1)
myList.append(4)
print(myList.is_empty())
print(myList.is_full())
print(myList.tail.data)
