# CS 3310 Assignment 1 by Christian Henning
# This program takes an input string of parenthesis, "(" or ")"
# and determines if they are balanced.

class Node(object):
    # constructor for Node class
    def __init__(self, data: any):
        self.data = data
        self.next: Node | None = None  # next node in list
        self.prev: Node | None = None  # previous node in list
    
    
class LinkedList(object):
    __head = None
    __tail = None
    __capacity = 0
    __size = 0

    # constructor for LinkedList class
    def __init__(self):
        # code goes here
        pass

    # add item x to list at index i
    def add(self, i, x):
        # code goes here
        pass

    # remove item at index i from the list
    def remove(self, i):
        # code goes here (should return item from list or None if item is not in the list)
        pass


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
        return self.__stackPointer + 1 == Stack.__maxSize

    # clears the stack
    def clear(self):
        # code goes here
        pass

    # looks at the top item of the stack without removing it
    def peek(self):
        # code goes here
        pass


class StackParenthesesChecker(object):
    __stack = None

    # constructor for StackParenthesesChecker class
    def __init__(self):
        # code goes here
        pass
    
    # Check if string s has balanced parenthesis
    def is_balanced(self, s):
        # code goes here
        pass


if __name__ == "__main__":
    inputParens = input('Input parenthesises: ')
    Parens = Stack()
    for ch in inputParens:
        if ch == '(' or ch == ')':
            Parens.push(ch)
