import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_code_tree(node, binary_str=''):
    if node is None:
        return {}
    if node.left is None and node.right is None:
        return {node.char: binary_str}

    code_dict = {}
    code_dict.update(huffman_code_tree(node.left, binary_str + '0'))
    code_dict.update(huffman_code_tree(node.right, binary_str + '1'))
    return code_dict

def huffman_encoding(data):
    frequency = Counter(data)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    root = heap[0]
    return huffman_code_tree(root)

data = input("Enter the text to encode: ")
huffman_codes = huffman_encoding(data)
print(f"Huffman Codes: {huffman_codes}")
encoded_str = ''.join([huffman_codes
