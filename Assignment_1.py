# CS 3310 Assignment 1 by Christian Henning
# This program takes an input string of parenthesis, "(" or ")"
# and determines if they are balanced.

class Node(object):
    __data = None
    __prev = None
    __next = None

    # constructor for Node class
    def __init__(self):
        # code goes here
        pass
    
    
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
    __linkedList = None
    __top = None

    # constructor for stack class
    def __init__(self):
        # code goes here
        pass

    # push item onto stack
    def push(self, x):
        # code goes here
        pass

    # pops item from top of stack
    def pop(self):
        # code goes here (should return item from top of stack or None if stack is empty)
        pass

    # returns Boolean of whether stack is currently empty
    def is_empty(self):
        # code goes here
        pass

    # returns Boolean of whether stack is currently full
    def is_full(self):
        # code goes here
        pass

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
