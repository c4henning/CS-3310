"""
CS 3310 Assignment 4 by Christian Henning

This program reads data from an input file, stores it in a LinkedList,
and performs a linear search and binary search.
"""

import csv
import time
import random


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
        """
        Together with `__next__` makes the LinkedList class iterable
        """
        self.i = self.__header.next
        return self

    def __next__(self):
        """
        Together with `__iter__` makes the LinkedList class iterable
        """
        n = self.i
        self.i = self.i.next
        if n == self.__trailer:
            raise StopIteration
        else:
            return n

    def __len__(self):
        """
        Allows for the use of the builtin `len()` function.

        Returns:
             int: The length of the LinkedList exclusive of header and trailer
        """
        return self.size

    def __contains__(self, item):
        """
        Executes a linear search for an item in the LinkedList.
        Allows for the use of the `in` operator to check for membership.

        Args:
            item: The item to search for.
        Returns:
            bool: True if item is found, otherwise False.
        """
        checked_node = self.__header.next
        while True:
            if checked_node == self.__trailer:
                return False
            elif checked_node.data == item:
                return True
            else:
                checked_node = checked_node.next

    def __getitem__(self, item):
        """
        Executes a linear search for an item in the LinkedList.
        Allows for the use of the `[]` subscript operator to access elements of the LinkedList.

        Args:
            item: The item to search for.
        Returns:
            any: The `data` attribute of the found Node
        """
        checked_node = self.__header.next
        while True:
            if checked_node == self.__trailer:
                return None
            elif checked_node.data == item:
                return checked_node.data
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

    def swap(self, a: int, b: int):
        if a == b:
            return  # No swap needed if the indices are the same

        if a > b:
            a, b = b, a  # Ensure a is the smaller index

        node_a = self.get_node(a)
        node_b = self.get_node(b)

        if b == a + 1:
            # Swapping adjacent nodes
            node_a_l = node_a.prev
            node_b_r = node_b.next

            node_a_l.next = node_b
            node_b.prev = node_a_l

            node_b.next = node_a
            node_a.prev = node_b

            node_a.next = node_b_r
            node_b_r.prev = node_a

        else:
            # Swapping non-adjacent nodes
            node_a_l = node_a.prev
            node_a_r = node_a.next

            node_b_l = node_b.prev
            node_b_r = node_b.next

            node_a_l.next, node_b_l.next = node_b, node_a
            node_a_r.prev, node_b_r.prev = node_b, node_a

            node_a.next, node_b.next = node_b_r, node_a_r
            node_a.prev, node_b.prev = node_b_l, node_a_l

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

    def index(self, item) -> int:
        """

        Args:
            item:
        Returns:
             int: The first index location of the specified item
        Raises:
            ValueError: If the item is not in the LinkedList
        """
        checked_node = self.__header.next
        index = 0
        while True:
            if checked_node == self.__trailer:
                raise ValueError(f"{item} is not in list")
            elif checked_node.data == item:
                return index
            else:
                checked_node = checked_node.next
                index += 1


class Game(object):
    def __init__(self, game_id, name, average_user_rating, user_rating_count, developer, size):
        """
        Initializes a Game object with the provided attributes.

        Args:
            game_id (int): The unique identifier for the game.
            name (str): The name of the game.
            average_user_rating (float): The average user rating for the game.
            user_rating_count (int): The count of user ratings for the game.
            developer (str): The developer of the game.
            size (int): The size of the game in bytes.
        """
        self.__game_id = int(game_id)
        self.__name = name
        self.__average_user_rating = float(average_user_rating)
        self.__user_rating_count = int(user_rating_count)
        self.__developer = developer
        self.__size = int(size)

    def __str__(self):
        """
        Returns a string representation of the Game object.
        """
        return ", ".join(str(value) for value in vars(self).values())

    def __eq__(self, other: 'Game'):
        """
        Checks if two Game objects are equal based on their game_id.

        Args:
            other (Game): The other Game object to compare to.

        Returns:
            bool: True if the game_id of both objects is equal, False otherwise.
        """
        return self.__game_id == other.__game_id

    def get(self):
        """
        Returns:
            list: A list containing all the attributes of the Game object.
        """
        all_data = [
            self.__game_id,
            self.__name,
            self.__average_user_rating,
            self.__user_rating_count,
            self.__developer,
            self.__size
        ]
        return all_data


def timing_function(func, *args, **kwargs):
    """
    Measures and prints the execution time of a function.

    Args:
        func (Callable): The function to be timed.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.

    Returns:
        The result of the function call.
    """
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    print(f"Time for {func.__name__}: {(end - start) * 10 ** 9:,.0f} ns")
    return result


def read_data_to_ll(ll: LinkedList) -> None:
    """
    Reads data from a CSV file and populates a LinkedList with Game objects.

    Args:
        ll (LinkedList): The LinkedList to be populated with Game objects.
    """
    with open("Assignments/games.csv") as file:
        file.readline()  # Skip the header
        games_file = csv.reader(file)
        for row in games_file:
            new_game = Game(*row)

            # If the new_game is not already in the LinkedList, add it to the end
            if new_game not in ll:
                ll.add(-1, new_game)
            # If the new_game is a duplicate with a higher score than an existing game, replace it
            elif ll[new_game].get()[3] < new_game.get()[3]:
                ll.remove(ll.index(new_game))
                ll.add(-1, new_game)
            # Otherwise, do nothing (new_game is a duplicate with a lower score)
            else:
                pass


def insertion_sort(ll: LinkedList, sort_by: int) -> None:
    """
    Sorts the LinkedList using the insertion sort algorithm.

    Args:
        ll (LinkedList): The LinkedList to be sorted.
        sort_by (int): The column in the `Game` data to sort the list by.
    """
    for i in range(1, len(ll)):
        current = ll.get_node(i)
        current_data = current.data
        j = i - 1

        # Find position where current node should be inserted
        while j >= 0 and current_data.get()[sort_by] < ll.get_node(j).data.get()[sort_by]:
            j -= 1

        # Remove current node and insert it at the found position
        if j != i - 1:
            ll.remove(i)
            ll.add(j + 1, current_data)


def partition(ll: LinkedList, sort_by: int, low_index: int, high_index: int) -> int:
    """
    Partitions the LinkedList in the specified range using the best-of-three pivot selection method.

    Args:
        ll (LinkedList): The LinkedList to be partitioned.
        sort_by (int): The column in the `Game` data to sort the list by.
        low_index (int): The starting index of the partition.
        high_index (int): The ending index of the partition.

    Returns:
        int: The index of the pivot element after partitioning.
    """
    # Best of three partitioning
    mid_index = (high_index + low_index) // 2
    candidate_a = ll.get_node(high_index).data.get()[sort_by]
    candidate_b = ll.get_node(mid_index).data.get()[sort_by]
    candidate_c = ll.get_node(low_index).data.get()[sort_by]

    if (candidate_a > candidate_b) != (candidate_a > candidate_c):
        pivot_value = candidate_a
    elif (candidate_b < candidate_a) != (candidate_b < candidate_c):
        pivot_value = candidate_b
    else:
        pivot_value = candidate_c

    # Find index of pivot_value
    if pivot_value == candidate_a:
        pivot_index = high_index
    elif pivot_value == candidate_b:
        pivot_index = mid_index
    else:
        pivot_index = low_index

    # Move the pivot element to the end
    ll.swap(pivot_index, high_index)

    i = low_index - 1
    for j in range(low_index, high_index):
        if ll.get_node(j).data.get()[sort_by] <= pivot_value:
            i += 1
            ll.swap(i, j)

    ll.swap(i + 1, high_index)

    return i + 1


def quick_sort(ll: LinkedList, sort_by, low_index, high_index) -> None:
    """
    Sorts the LinkedList in the specified range recursively using the QuickSort algorithm.

    Args:
        ll (LinkedList): The LinkedList to be sorted.
        sort_by (int): The column in the 'Game' data to sort the list by.
        low_index (int): The starting index of the range to be sorted.
        high_index (int): The ending index of the range to be sorted.
    """
    if low_index < high_index:
        pivot_index = partition(ll, sort_by, low_index, high_index)
        quick_sort(ll, sort_by, low_index, pivot_index - 1)  # Sort the left sublist
        quick_sort(ll, sort_by, pivot_index + 1, high_index)  # Sort the right sublist


# Task 1, 2
gamesLinkedList = LinkedList()
read_data_to_ll(gamesLinkedList)
print("Number of elements in LinkedList: ", len(gamesLinkedList))

# Task 3
print("\n*** Linear Search Test ***\n")

print("Before sorting:\n"
      "First 5 elements from linked list:")
for i in range(5):
    game = gamesLinkedList.get_node(i)
    data = game.data
    print(data)

print("\nSingle search:")
game_to_find = random.choice(list(gamesLinkedList)).data.get()[1]
print(f"Searching for {game_to_find}...")

start = time.perf_counter()
for game in gamesLinkedList:
    # The `__contains__` dunder was hand-coded for the LL class, and executes a linear search.
    # Although the following loop appears to use a primitive list, it doesn't.
    # This allows us to write more naturally using the `for x in y` syntax.
    if game.data.get()[1] == game_to_find:
        print(game.data)
        break
end = time.perf_counter()
meas_time = (end - start) * 10 ** 9

print(f"{game_to_find if len(game_to_find) < 20 else game_to_find[:20].rstrip(' ') + '...'}"
      f" was found in {meas_time:,.0f} ns")


# Task 4
print("\nMultiple search:")
games_to_search_for = []
print("Searching for:")
for _ in range(10):
    game_to_find = random.choice(list(gamesLinkedList))
    game_name = game_to_find.data.get()[1]
    print("\t", game_name)
    games_to_search_for.append(game_name)

recd_times = []
for target in games_to_search_for:
    start = time.perf_counter()

    for game in gamesLinkedList:
        if game.data.get()[1] == target:
            break

    end = time.perf_counter()
    meas_time = (end - start) * 10 ** 9
    recd_times.append(meas_time)

print(f"\nAverage linear search time of gamesLinkedList across {len(recd_times)} iterations is:\n"
      f"\t {sum(recd_times)/len(recd_times):,.0f} ns")


# Task 5
print()
timing_function(quick_sort, gamesLinkedList, 1, 0, len(gamesLinkedList) - 1)    # quick_sort by Name
timing_function(insertion_sort, gamesLinkedList, 1)     # insertion_sort by Name
# sorting by the same col isn't very representative as an already sorted list is an edge case
# I ran quick_sort first for its better average case time complexity
# then insertion_sort due to its best case time complexity

print("\nAfter sorting:\n"
      "First 5 elements from linked list:")
for i in range(5):
    game = gamesLinkedList.get_node(i)
    data = game.data
    print(data)

print()
