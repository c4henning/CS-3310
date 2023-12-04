# CS 3310 Assignment 3 by Christian Henning
# This program implements the Huffman Codes algorithm, and displays a table with
# the resulting codes, associated information, and weighted minimum path length.

import heapq

# Read in frequencies and characters
freq = [77, 17, 32, 42, 120, 24, 17, 50, 76, 4, 7, 42, 24, 67, 67, 20, 5, 59, 67, 85, 37, 12, 22, 4, 22, 2]
chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']

if len(freq) != len(chars):
    raise ValueError("Mismatched lengths: Frequency list has %d elements, while Characters list has %d elements."
                     % (len(freq), len(chars)))


class Node:
    """
    This class represents a Node in a Huffman tree.

    Args:
        freq (int): Frequency of the character.
        char (any | None): The character associated with the node (if any).
        left (Node | None): Left child node.
        right (Node | None): Right child node.
    """
    def __init__(self, freq: int, char: any = None, left: 'Node' = None, right: 'Node' = None):
        # freq comes first as it is the only required argument
        # char, left, and right are optional arguments
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __str__(self):
        """
        Convert the Node (and all children) to a string representation.
        """
        return self._str_helper(self)

    def _str_helper(self, node, depth=0):
        """
        Helper function for creating a visual representation of the tree structure.

        Args:
            node (Node): Current node.
            depth (int): Depth of the current node in the tree.

        Returns:
            str: String representation of the node and its children.
        """
        # Base case for recursion exit
        if node is None:
            return ""

        # Adds indentation for every level down the tree
        indent = "│   " * depth

        # Here we use a preorder traversal w/ recursion
        result = f"{indent}freq: {node.freq}, char: {node.char}\n"
        result += self._str_helper(node.left, depth + 1)
        result += self._str_helper(node.right, depth + 1)

        return result

    def __lt__(self, other: 'Node'):
        """
        Custom less-than comparison method for Node instances based on freq.

        Args:
            other (Node): Another Node instance to compare against.

        Returns:
            bool: True if the frequency of the current node is less than the frequency of the other node.
        """
        return self.freq < other.freq


def create_huffman_tree(freq: list, chars: list) -> Node:
    """
    Creates a Huffman tree from the given lists of frequencies and characters.

    Args:
        freq (list): List of integers representing the frequencies of characters.
        chars (list): List of characters corresponding to their frequencies.

    Returns:
        Node: The root of the Huffman tree.
    """
    # Create a list of Node instances for each character and its frequency
    heap = [Node(f, c) for f, c in zip(freq, chars)]
    # Convert the list into a min-heap
    heapq.heapify(heap)

    # Build the Huffman tree by merging nodes with the smallest frequencies
    while len(heap) > 1:
        node1 = heapq.heappop(heap)     # Current smallest
        node2 = heapq.heappop(heap)     # 2nd smallest

        # Create a new node with the sum of frequencies
        merged_node = Node(node1.freq + node2.freq)
        # Assign left and right children
        merged_node.left = node1
        merged_node.right = node2
        # Push the merged node back onto our min-heap
        heapq.heappush(heap, merged_node)

    # The root of the Huffman tree is the only remaining node in the heap
    return heap[0]


def create_huffman_codes(root: Node, code="", huff_dict=None) -> dict:
    """
    Traverse the Huffman tree and assign binary codes to each character.

    Each element in the resulting dict is a key-value pair where the key is the alpha `char`
    and the value is the composed binary huffman code.

    Args:
        root (Node): The root of the Huffman tree.
        code (str): The binary code assigned to the current node. (Used in recursive case only)
        huff_dict (dict): A dictionary to store the Huffman codes. (Used in recursive case only)

    Returns:
        dict: A dictionary where keys are characters and values are their corresponding Huffman codes.
    """
    # Instantiate the dictionary if not provided (i.e. first pass before recursion)
    if huff_dict is None:
        huff_dict = {}

    # Preorder traversal for copying of the tree's contents
    # Uses recursion for nodes
    if root.char:
        huff_dict[root.char] = code
    if root.left:
        create_huffman_codes(root.left, code + "0", huff_dict)
    if root.right:
        create_huffman_codes(root.right, code + "1", huff_dict)

    return huff_dict


def print_output(freq: list, chars: list, codes: dict):
    """
    Output the Huffman coding results alphabetically with the weighted minimum path length in a table.

    Args:
        freq (list): List of integers representing the frequencies of characters.
        chars (list): List of characters corresponding to their frequencies.
        codes (dict): The dictionary of our previously generated Huffman codes.
    """
    # Output the results table
    weighted_min_path_length = 0
    print("╒════════╤═══════════╤════════════╤════════╤════════════╕\n"
          "│ Letter │ Frequency │    Code    │ Length │ Freq X Len │\n"
          "├╶╶╶╶╶╶╶╶┼╶╶╶╶╶╶╶╶╶╶╶┼╶╶╶╶╶╶╶╶╶╶╶╶┼╶╶╶╶╶╶╶╶┼╶╶╶╶╶╶╶╶╶╶╶╶┤")

    # Iterate over characters in alphabetical order
    for char in sorted(chars):
        # Match char to freq with index
        frequency = freq[chars.index(char)]

        # Unpack code from dictionary
        code = codes[char]

        # Calculate length
        length = len(code)

        # Calculate min path length
        freq_x_len = frequency * length
        weighted_min_path_length += freq_x_len

        print(f"│ {char:^6} │ {frequency:^9} │ {code:<10} │ {length:^6} │ {freq_x_len:^10} │")

    # Output the weighted minimum path length
    print(f"╞════════╧═══════════╧════════════╧════════╧════════════╡\n"
          f"│ The weighted minimum path length is:   {weighted_min_path_length: >10}     │\n"
          f"╰───────────────────────────────────────────────────────╯")


if __name__ == '__main__':
    # Here we go!
    huffman_tree = create_huffman_tree(freq, chars)
    huffman_codes = create_huffman_codes(huffman_tree)
    print_output(freq, chars, huffman_codes)

    you_are_curious = False  # Change me for bonus content
    if you_are_curious:
        if input("Print huffman codes dict? y/n: ").lower().startswith('y'):
            print(huffman_codes)
        if input("Print tree? y/n: ").lower().startswith('y'):
            print(huffman_tree)
        while True:
            if input("Encode a word? y/n: ").lower().startswith('y'):
                word = input("\tinput a word: ")
                print(f'\t\t{word}: ', end='')
                for ch in word:
                    print(huffman_codes[ch.upper()], end='')
                print()
            else:
                print("Bye!")
                break
