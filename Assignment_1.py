# CS 3310 Assignment 1 by Christian Henning
# This program takes an input string of parenthesis, "(" or ")"
# and determines if they are balanced.

# initialize toggle for verbose output
verbose = False


class Node(object):
    """
    This class represents a node in a linked list.

    Attributes:
        data (any): The data stored in the node.
        next (Node | None): Reference to the next node in the list.
        prev (Node | None): Reference to the previous node in the list.
    """
    def __init__(self, data: any = None):
        """
        Initializes a new Node instance.

        Args:
            data (any, optional): The data to be stored in the node. Defaults to None.
        """
        self.data = data
        self.next: Node | None = None  # next node in list
        self.prev: Node | None = None  # previous node in list


class LinkedList(object):
    """
    This class represents a linked list data structure.

    Attributes:
        __maxSize (int): An arbitrary maximum size to limit the project's scope.
        __header (Node): The header node of the linked list.
        __trailer (Node): The trailer node of the linked list.
        size (int): The current size of the linked list.
    """
    __maxSize = 50

    # constructor for LinkedList class
    def __init__(self):
        self.__header = Node()
        self.__trailer = Node()
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header
        self.size = 0
        if verbose:
            print("Initialized Linked List")

    # add item x to list at index i
    def add(self, index: int, new_data: any):
        """
        Adds a new Node with data `new_data` to the linked list at index `i`.

        Args:
            index (int): The index at which to add the new item.
            new_data (any): The data to be stored in the new node.
        Raises:
            IndexError: If the linked list is full (__maxSize is reached).
        """
        if self.size == self.__maxSize:
            raise IndexError("An attempt to insert was made while Linked List is full")
        else:
            new_node = Node(new_data)
            next_node = self.get_node(index)
            prev_node = next_node.prev

            new_node.next = next_node
            new_node.prev = prev_node

            next_node.prev = new_node

            prev_node.next = new_node

            self.size += 1
            if verbose:
                print(f"Added Node: {id(new_node)}\n"
                      f"\twith data: {new_data}\n"
                      f"\ttype: {type(new_data)}")

    # remove item at index i from the list
    def remove(self, index) -> any:
        """
        Removes the Node at the specified index in the linked list.

        Args:
            index (int): The index of the item to be removed.
        Returns:
            any: The data stored in the removed node.
        Raises:
            IndexError: If the linked list is empty.
        """
        if self.size == 0:
            raise IndexError("An attempt to delete was made while Linked List is empty")
        else:
            target_node = self.get_node(index)
            data = target_node.data

            next_node = target_node.next
            prev_node = target_node.prev
            next_node.prev = prev_node
            prev_node.next = next_node

            del target_node
            self.size -= 1
            return data

    # find node at specified index
    def get_node(self, index) -> Node:
        """
        Finds and returns the Node at the specified index.

        Args:
            index (int): The index of the Node to retrieve.
        Returns:
            Node: The Node at the specified index.
        Raises:
            IndexError: If the index is out of range.
        """
        # support for negative indexing
        if index < 0:
            index += self.size + 1
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        current = self.__header.next
        # tabs through list until specified index is reached
        for _ in range(index):
            current = current.next
        return current


class Stack(object):
    """
    A stack data structure with a fixed maximum size.

    Attributes:
        __maxSize (int): An arbitrary maximum size to limit the project's scope.
        size (int): The current size of the linked list.

    """
    __maxSize = 50  # Arbitrary max size to limit scope of project

    # constructor for stack class
    def __init__(self):
        # code goes here
        self.__stack = [None] * Stack.__maxSize
        self.__stackPointer = -1
        if verbose:
            print("Initialized stack")

    # push item onto stack
    def push(self, item: any):
        """
        Pushes an item onto the top of the stack.

        Args:
            item (any): The item to be pushed onto the stack.

        Raises:
            IndexError: If the stack is already full.
        """
        if self.is_full():
            raise IndexError("stack is full")
        else:
            self.__stackPointer += 1
            self.__stack[self.__stackPointer] = item
            if verbose:
                print(f"pushed item: {item}")

    # pops item from top of stack
    def pop(self) -> any:
        """
        Pops and returns the item from the top of the stack.

        Returns:
            any: The item popped from the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("stack is empty")
        else:
            item = self.__stack[self.__stackPointer]
            self.__stackPointer -= 1
            if verbose:
                print(f"popped item: {item}")
            return item

    # returns Boolean of whether stack is currently empty
    def is_empty(self) -> bool:
        """
        Checks if the stack is currently empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.__stackPointer < 0

    # returns Boolean of whether stack is currently full
    def is_full(self) -> bool:
        """
        Checks if the stack is currently full.

        Returns:
            bool: True if the stack is full, False otherwise.
        """
        return self.__stackPointer + 1 >= Stack.__maxSize

    # clears the stack
    def clear(self):
        """
        Clears the stack by resetting the stack pointer to -1.
        """
        self.__stackPointer = -1

    # looks at the top item of the stack without removing it
    def peek(self):
        """
        Retrieves and returns the item at the top of the stack without removing it.

        Returns:
            any: The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("stack is empty")
        else:
            item = self.__stack[self.__stackPointer]
            if verbose:
                print(f"top item: {item}")
            return item


class StackParenthesesChecker(object):
    # constructor for StackParenthesesChecker class
    def __init__(self):
        self.__stack = Stack()

    # Check if string s has balanced parenthesis
    def is_balanced(self, lst: LinkedList):
        if verbose:
            print("Checking if balanced...")
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
        inputParens = input("(Q)uit, toggle (V)erbosity, or Input parenthesis: ")

        if inputParens.upper() == 'Q':
            break
        if inputParens.upper() == 'V':
            verbose ^= True
            print(f"Verbose mode: {'ON' if verbose else 'OFF'}")
        else:
            Parens = LinkedList()
            print("--------------------\n"
                  "Stack implementation")
            for ch in inputParens:
                if ch == '(' or ch == ')':
                    # add to end of list
                    Parens.add(-1, ch)

            result = StackParenthesesChecker()
            print(f"Result of string '{inputParens}': {'balanced' if result.is_balanced(Parens) else 'unbalanced'}\n"
                  f"--------------------")
