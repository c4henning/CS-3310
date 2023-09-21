class Node:
    def __init__(self, data: any):
        self.data = data
        self.next: Node | None = None   # next node in list
        self.prev: Node | None = None   # previous node in list


class LinkedList:
    def __init__(self, max_size: int):
        self.max_size = max_size         # maximum allowable nodes
        self.head: Node | None = None   # first node in list
        self.tail: Node | None = None   # last node in list
        self.size: int = 0              # total nodes in list

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size >= self.max_size

    def append(self, new_data):
        if not self.is_full():
            new_node = Node(new_data)

            if self.is_empty():  # special case for empty list
                self.head = new_node  # only node == head & tail
                self.tail = new_node
                self.size += 1
            else:
                self.tail.next = new_node  # add next node to old tail
                new_node.prev = self.tail  # add old tail as .prev for new node
                self.tail = new_node  # reset tail to be new node
                self.size += 1

            print(f"Added Node: {new_node}\n\twith data: {new_data}")

        else:
            print("Unable to complete; List is full.")

    def prepend(self, new_data):
        if not self.is_full():
            new_node = Node(new_data)

            if self.is_empty():  # special case for empty list
                self.head = new_node  # only node == head & tail
                self.tail = new_node
                self.size += 1
            else:
                self.head.prev = new_node  # add prev node to old head
                new_node.next = self.tail  # add old head as .next for new node
                self.head = new_node  # reset head to be new node
                self.size += 1

            print(f"Added Node: {new_node}\n\twith data: {new_data}")

        else:
            print("Unable to complete; List is full.")

    def find(self, data):
        if data =

    def swap(self, old_data, new_data):
        pass
