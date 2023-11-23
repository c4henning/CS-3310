# CS 3310 Assignment 4 by Christian Henning
# This program reads data from an input file, stores it in a LinkedList,
# and performs a linear search and binary search.
import csv


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
    __maxSize = 9_999_999

    def __init__(self):
        self.__header = Node()
        self.__trailer = Node()
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header
        self.size = 0

    def __iter__(self):
        self.i = self.__header.next
        return self

    def __next__(self):
        n = self.i
        self.i = self.i.next
        if n == self.__trailer:
            raise StopIteration
        else:
            return n

    def __len__(self):
        return self.size

    def __contains__(self, item):
        checked_node = self.__header.next
        while True:
            if checked_node == self.__trailer:
                return False
            elif checked_node.data == item:
                return True
            else:
                checked_node = checked_node.next

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


class Game:
    def __init__(self, game_id, name, average_user_rating, user_rating_count, developer, size):
        self.__game_id = int(game_id)
        self.__name = name
        self.__average_user_rating = float(average_user_rating)
        self.__user_rating_count = int(user_rating_count)
        self.__developer = developer
        self.__size = int(size)

    def __repr__(self):
        return f'{self.__game_id, self.__name, self.__average_user_rating, self.__user_rating_count, self.__developer, self.__size}'

    def __eq__(self, other: 'Game'):
        return self.__game_id == other.__game_id

    def get(self):
        all_data = [
            self.__game_id,
            self.__name,
            self.__average_user_rating,
            self.__user_rating_count,
            self.__developer,
            self.__size
        ]
        return all_data


def read_data_to_ll(ll: LinkedList) -> None:
    with open("Assignments/games.csv") as file:
        file.readline()     # waste header
        games_file = csv.reader(file)
        for row in games_file:
            new_game = Game(*row)
            if new_game not in ll:
                ll.add(-1, new_game)


gamesLinkedList = LinkedList()
read_data_to_ll(gamesLinkedList)
