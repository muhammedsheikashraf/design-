"""Question 5: Huffman Coding."""
import heapq
from collections import Counter


class Node:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def huffman_coding(text):
    if not text:
        return {}

    frequency = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(None, left.frequency + right.frequency)
        parent.left = left
        parent.right = right
        heapq.heappush(heap, parent)

    root = heap[0]
    codes = {}

    def make_codes(node, code):
        if node.char is not None:
            codes[node.char] = code or "0"
            return
        make_codes(node.left, code + "0")
        make_codes(node.right, code + "1")

    make_codes(root, "")
    return codes


if __name__ == "__main__":
    text = "aaabbc"
    codes = huffman_coding(text)
    print("Huffman codes:")
    for char, code in sorted(codes.items()):
        print(repr(char), ":", code)

    encoded = "".join(codes[char] for char in text)
    print("Encoded text:", encoded)
