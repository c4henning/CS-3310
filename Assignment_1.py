# CS 3310 Assignment 1 by Christian Henning
# This program takes an input string of parenthesis, "(" or ")"
# and determines if they are balanced.

# Initialize toggle for verbose output. If toggled (by user in main loop), it
# will print various debugging statements that report the actions of functions
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

    def __init__(self):
        self.__header = Node()
        self.__trailer = Node()
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header
        self.size = 0
        if verbose:
            print("Initialized Linked List:", id(self))

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
                      f"\tto parent list: {id(self)}\n"
                      f"\twith data: {new_data}\n"
                      f"\ttype: {type(new_data)}")

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

            if verbose:
                print(f"Removed Node: {id(target_node)}\n"
                      f"\tfrom parent list: {id(self)}")
            del target_node
            self.size -= 1
            return data

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
        __stackPointer (int): The current index of the top of stack.

    """
    __maxSize = 50  # Arbitrary max size to limit scope of project

    def __init__(self):
        """
        Initializes a new stack with an empty linked list and a stack pointer set to -1.
        """
        self.__linked_list = LinkedList()
        self.__stackPointer = -1
        if verbose:
            print("Initialized Stack:", id(self))

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
            self.__linked_list.add(self.__stackPointer, item)
            if verbose:
                print(f"Pushed item: {item}\n"
                      f"\tto Stack: {id(self)}")

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
            item = self.__linked_list.remove(self.__stackPointer)
            self.__stackPointer -= 1
            if verbose:
                print(f"Popped item: {item}\n"
                      f"\tfrom Stack: {id(self)}")
            return item

    def is_empty(self) -> bool:
        """
        Checks if the stack is currently empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        result = self.__stackPointer < 0
        if verbose:
            print(f"Is stack {id(self)} empty?", result)
        return result

    def is_full(self) -> bool:
        """
        Checks if the stack is currently full.

        Returns:
            bool: True if the stack is full, False otherwise.
        """
        result = self.__stackPointer + 1 >= Stack.__maxSize
        if verbose:
            print(f"Is stack {id(self)} full?", result)
        return result

    def clear(self):
        """
        Clears the stack by resetting the stack pointer to -1.
        """
        self.__stackPointer = -1

    def peek(self):
        """
        Retrieves and returns the item at the top of the stack without removing it.

        Returns:
            any: The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            return None
        else:
            item = self.__linked_list.get_node(self.__stackPointer).data
            if verbose:
                print(f"top item: {item}")
            return item


class StackParenthesesChecker(object):
    """
    A class for checking balanced parentheses using a stack data structure.

    Attributes:
        __stack (Stack): An instance of the Stack class used for storing parentheses.

    """

    def __init__(self):
        self.__stack = Stack()

    def is_balanced(self, string: str):
        """
        Checks if the given linked list of parentheses is balanced.

        Args:
            string (str): The string containing the parentheses to be checked.

        Returns:
            bool: True if the parentheses are balanced, False otherwise.

        """
        if verbose:
            print("Checking if balanced...")

        # Loop through the linked list and process each parenthesis
        for paren in string:
            try:
                if paren == '(':
                    self.__stack.push(paren)
                elif paren == ')':
                    # If a closing parenthesis is encountered, pop from the stack
                    self.__stack.pop()
            except IndexError:
                # An IndexError occurs if there's a mismatched closing parenthesis
                return False

        # The stack should be empty if all parentheses are balanced
        return self.__stack.is_empty()


class Queue(object):
    """
    A queue data structure with a fixed maximum size.

    Attributes:
        __maxSize (int): An arbitrary maximum size to limit the project's scope.
        __linked_list (LinkedList): A linked list used to store items in the queue.
        __front (int): The current index of the front of the queue.
        __rear (int): The current index of the rear of the queue.

    """
    __maxSize = 50  # Arbitrary max size to limit scope of project

    def __init__(self):
        self.__linked_list = LinkedList()
        self.__front = 0
        self.__rear = -1
        if verbose:
            print("Initialized Queue", id(self))

    def enqueue(self, item):
        """
        Adds an item to the rear of the queue.

        Args:
            item (any): The item to be added to the queue.

        Raises:
            IndexError: If the queue is already full.
        """
        if self.is_full():
            raise IndexError("queue is full")
        else:
            self.__rear += 1
            self.__linked_list.add(self.__rear, item)
            if verbose:
                print(f"Added item: {item}\n"
                      f"\tto Queue: {id(self)}")

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue.

        Returns:
            any: The item removed from the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("queue is empty")
        else:
            item = self.__linked_list.get_node(self.__front)
            self.__front += 1
            if verbose:
                print(f"Removed item: {item.data}\n"
                      f"\tfrom Queue: {id(self)}")
            return item

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        result = self.__front > self.__rear
        if verbose:
            print(f"Is queue {id(self)} empty?", result)
        return result

    def is_full(self):
        """
        Checks if the queue is currently full.

        Returns:
            bool: True if the queue is full, False otherwise.
        """
        result = self.__rear - self.__front >= Queue.__maxSize
        if verbose:
            print(f"Is queue {id(self)} full?", result)
        return result

    def clear(self):
        """
        Clears the queue by replacing it with a new empty linked list and resetting the pointers.
        """
        del self.__linked_list
        self.__linked_list = LinkedList()
        self.__front = 0
        self.__rear = -1

    def poll(self):
        """
        Retrieves and returns the item at the front of the queue without removing it.

        Returns:
            any: The item at the front of the queue, None if the queue is empty.
        """
        if self.is_empty():
            return None
        else:
            item = self.__linked_list.get_node(self.__front).data
            if verbose:
                print(f"first in queue: {item}")
            return item


class QueueParenthesesChecker(object):
    """
    A class for checking balanced parentheses using a queue data structure.

    Attributes:
        __queue (Queue): An instance of the Queue class used for storing parentheses.

    """

    def __init__(self):
        self.__queue = Queue()

    def is_balanced(self, string: str):
        """
        Checks if the given linked list of parentheses is balanced.

        Args:
            string (str): The string containing the parentheses to be checked.

        Returns:
            bool: True if the parentheses are balanced, False otherwise.

        """
        if verbose:
            print("Checking if balanced...")

        # Loop through the linked list and process each parenthesis
        for paren in string:
            try:
                if paren == '(':
                    self.__queue.enqueue(paren)
                elif paren == ')':
                    # If a closing parenthesis is encountered, pop from the stack
                    self.__queue.dequeue()
            except IndexError:
                # An IndexError occurs if there's a mismatched closing parenthesis
                return False

        # The stack should be empty if all parentheses are balanced
        return self.__queue.is_empty()


# Main loop. This is where the initial calls are made and inputs are taken
if __name__ == "__main__":
    # Loop continues until (Q)uit command is issued
    while True:
        parens = input("(Q)uit, toggle (V)erbosity, or Input parenthesis: ")

        if parens.upper() == 'Q':
            break

        # XOR will toggle the verbose debugging mode
        if parens.upper() == 'V':
            verbose ^= True
            print(f"Verbose mode: {'ON' if verbose else 'OFF'}\n")

        else:
            print(f"\n"
                  f"╒══════════════════════════════\n"
                  f"│ Stack implementation")
            stackResult = StackParenthesesChecker()
            print(f"│ Result of string '{parens}':\n"
                  f"│ \t{'balanced' if stackResult.is_balanced(parens) else 'unbalanced'}")
            print(f"├╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶\n"
                  f"│ Queue implementation")
            queueResult = QueueParenthesesChecker()
            print(f"│ Result of string '{parens}':\n"
                  f"│ \t{'balanced' if queueResult.is_balanced(parens) else 'unbalanced'}\n"
                  f"└────────────────────\n")
