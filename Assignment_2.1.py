# CS 3310 Assignment 2 by Christian Henning

import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define a custom comparison method for Node instances
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(chars, freq):
    heap = [Node(c, f) for c, f in zip(chars, freq)]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged_node = Node(None, node1.freq + node2.freq)
        merged_node.left = node1
        merged_node.right = node2
        heapq.heappush(heap, merged_node)

    return heap[0]


def build_huffman_codes(root, code="", mapping=None):
    # Step 4: Traverse the Huffman tree to assign codes
    if mapping is None:
        mapping = {}

    if root.char:
        mapping[root.char] = (code, len(code))
    if root.left:
        build_huffman_codes(root.left, code + "0", mapping)
    if root.right:
        build_huffman_codes(root.right, code + "1", mapping)

    return mapping


def print_output(chars, freq, codes):
    # Step 5: Output the results
    weighted_min_path_length = 0
    print("╒════════╤═══════════╤══════════╤════════╤════════════╕")
    print("│ Letter │ Frequency │   Code   │ Length │ Freq X Len │")
    print("├╶╶╶╶╶╶╶╶┼╶╶╶╶╶╶╶╶╶╶╶┼╶╶╶╶╶╶╶╶╶╶┼╶╶╶╶╶╶╶╶┼╶╶╶╶╶╶╶╶╶╶╶╶┤")
    for char in sorted(chars):
        frequency = freq[chars.index(char)]
        code, length = codes[char]
        freq_x_len = frequency * length
        weighted_min_path_length += freq_x_len
        print(f"│ {char:^6} │ {frequency:^9} │ {code:<8} │ {length:^6} │ {freq_x_len:^10} │")

    print("╞════════╧═══════════╧══════════╧════════╧════════════╡")
    # Step 6: Output the weighted minimum path length
    print(f"│The weighted minimum path length is: {weighted_min_path_length: <15} │")
    print("╰─────────────────────────────────────────────────────╯")


# Step 1: Read in frequencies (assuming you've read from a file)
chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']
freq = [77, 17, 32, 42, 120, 24, 17, 50, 76, 4, 7, 42, 24, 67, 67, 20, 5, 59, 67, 85, 37, 12, 22, 4, 22, 2]

if __name__ == '__main__':
    huffman_tree = build_huffman_tree(chars, freq)
    huffman_codes = build_huffman_codes(huffman_tree)
    print_output(chars, freq, huffman_codes)
