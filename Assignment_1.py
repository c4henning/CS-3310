# CS 3310 Assignment 1 by Christian Henning
# This program takes an input string of parenthesis, "(" or ")"
# and determines if they are balanced.

class Node(object):
    # constructor for Node class
    def __init__(self, data: any = None):
        self.data = data
        self.next: Node | None = None  # next node in list
        self.prev: Node | None = None  # previous node in list
    

class LinkedList(object):
    __maxSize = 50      # Arbitrary max size to limit scope of project

    # constructor for LinkedList class
    def __init__(self):
        self.__header = Node()
        self.__trailer = Node()
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header
        self.size = 0

    # add item x to list at index i
    def add(self, i: int, x: any):
        if self.size == self.__maxSize:
            raise IndexError("An attempt to insert was made while Linked List is full")
        else:
            new_node = Node(x)
            next_node = self.get_node(i)
            prev_node = next_node.prev

            new_node.next = next_node
            new_node.prev = prev_node

            next_node.prev = new_node

            prev_node.next = new_node

            self.size += 1

    # remove item at index i from the list
    def remove(self, i):
        if self.size == 0:
            raise IndexError("An attempt to delete was made while Linked List is empty")
        else:
            target_node = self.get_node(i)
            data = target_node.data

            next_node = target_node.next
            prev_node = target_node.prev
            next_node.prev = prev_node
            prev_node.next = next_node

            del target_node
            self.size -= 1
            return data

    # find node at specified index
    def get_node(self, i):
        # support for negative indexing
        if i < 0:
            i += self.size + 1
        if i < 0 or i > self.size:
            raise IndexError("Index out of range")
        current = self.__header.next
        for _ in range(i):
            current = current.next
        return current

    # debug; kill when done
    def printoTesto(self):
        for i in range(self.size):
            node = self.get_node(i)
            print(node.data)
    # end debug


class Stack(object):
    __maxSize = 50      # Arbitrary max size to limit scope of project

    # constructor for stack class
    def __init__(self):
        # code goes here
        self.__stack = [None] * Stack.__maxSize
        self.__stackPointer = -1

    # push item onto stack
    def push(self, item: any):
        if self.is_full():
            raise IndexError("stack is full")
        else:
            self.__stackPointer += 1
            self.__stack[self.__stackPointer] = item
            print(f"pushed item: {item}")

    # pops item from top of stack
    def pop(self) -> any:
        if self.is_empty():
            raise IndexError("stack is empty")
        else:
            item = self.__stack[self.__stackPointer]
            self.__stackPointer -= 1
            print(f"popped item: {item}")
            return item

    # returns Boolean of whether stack is currently empty
    def is_empty(self) -> bool:
        return self.__stackPointer < 0

    # returns Boolean of whether stack is currently full
    def is_full(self) -> bool:
        return self.__stackPointer + 1 >= Stack.__maxSize

    # clears the stack
    def clear(self):
        self.__stackPointer = -1

    # looks at the top item of the stack without removing it
    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        else:
            item = self.__stack[self.__stackPointer]
            print(f"top item: {item}")
            return item


class StackParenthesesChecker(object):
    # constructor for StackParenthesesChecker class
    def __init__(self):
        self.__stack = Stack()

    # Check if string s has balanced parenthesis
    def is_balanced(self, lst: LinkedList):
        for _ in range(lst.size):
            try:
                next_paren = lst.remove(0)
                if next_paren == '(':
                    self.__stack.push(next_paren)
                elif next_paren == ')':
                    self.__stack.pop()
            except IndexError:
                return False

        return self.__stack.is_empty()


if __name__ == "__main__":
    while True:
        inputParens = input('(Q)uit or Input parenthesis: ')

        if inputParens.upper() == 'Q':
            break
        else:
            Parens = LinkedList()
            for ch in inputParens:
                if ch == '(' or ch == ')':
                    # add to end of list
                    Parens.add(-1, ch)

            result = StackParenthesesChecker()
            if result.is_balanced(Parens):
                print("Balanced")
            else:
                print("unbalanced")
