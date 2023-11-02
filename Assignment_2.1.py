# CS 3310 Assignment 3 by Christian Henning

import heapq

# Read in frequencies and characters
freq = [77, 17, 32, 42, 120, 24, 17, 50, 76, 4, 7, 42, 24, 67, 67, 20, 5, 59, 67, 85, 37, 12, 22, 4, 22, 2]
chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']


class Node:
    def __init__(self, freq: int, char: any = None, left: 'Node' = None, right: 'Node' = None):
        # freq first as the only required arg
        # char (and left/right) is optional
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __str__(self):
        return self._str_helper(self)

    def _str_helper(self, node, depth=0):
        # makes a nicely formatted, visual row hierarchy
        if node is None:
            return ""

        indent = "│   " * depth
        # preorder traverse w/ recursion
        result = f"{indent}freq: {node.freq}, char: {node.char}\n"
        result += self._str_helper(node.left, depth + 1)
        result += self._str_helper(node.right, depth + 1)
        return result

    def __lt__(self, other: 'Node'):
        # Define a custom comparison method for Node instances
        return self.freq < other.freq


def create_huffman_tree(freq: list, chars: list) -> Node:
    heap = [Node(f, c) for f, c in zip(freq, chars)]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged_node = Node(node1.freq + node2.freq)
        merged_node.left = node1
        merged_node.right = node2
        heapq.heappush(heap, merged_node)

    return heap[0]


def create_huffman_codes(root: Node, code="", huff_dict=None) -> dict:
    # Traverse the Huffman tree to assign codes

    # first iter, instantiate dict
    if huff_dict is None:
        huff_dict = {}

    # Preorder traversal for copying of the tree's contents
    # uses recursion for nodes
    if root.char:
        huff_dict[root.char] = code
    if root.left:
        create_huffman_codes(root.left, code + "0", huff_dict)
    if root.right:
        create_huffman_codes(root.right, code + "1", huff_dict)

    return huff_dict


def print_output(freq: list, chars: list, codes: dict):
    # Output the results
    weighted_min_path_length = 0
    print("╒════════╤═══════════╤══════════╤════════╤════════════╕\n"
          "│ Letter │ Frequency │   Code   │ Length │ Freq X Len │\n"
          "├╶╶╶╶╶╶╶╶┼╶╶╶╶╶╶╶╶╶╶╶┼╶╶╶╶╶╶╶╶╶╶┼╶╶╶╶╶╶╶╶┼╶╶╶╶╶╶╶╶╶╶╶╶┤")
    for char in sorted(chars):
        # match char to freq with index
        frequency = freq[chars.index(char)]

        # unpack from dict
        code = codes[char]

        # calculate length
        length = len(code)

        # calculate min path length
        freq_x_len = frequency * length
        weighted_min_path_length += freq_x_len

        print(f"│ {char:^6} │ {frequency:^9} │ {code:<8} │ {length:^6} │ {freq_x_len:^10} │")

    # Output the weighted minimum path length
    print(f"╞════════╧═══════════╧══════════╧════════╧════════════╡\n"
          f"│ The weighted minimum path length is: {weighted_min_path_length: >10}     │\n"
          f"╰─────────────────────────────────────────────────────╯")


if __name__ == '__main__':
    huffman_tree = create_huffman_tree(freq, chars)
    huffman_codes = create_huffman_codes(huffman_tree)
    print_output(freq, chars, huffman_codes)
    if input("Print tree? y/n: ") in ['y', 'Y']:
        print(huffman_tree)
