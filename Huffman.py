import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_tree(char_freq_tuples):
    heap = [Node(char, freq) for char, freq in char_freq_tuples]
    heapq.heapify(heap)

    while len(heap) > 1:
        left_node = heapq.heappop(heap)
        right_node = heapq.heappop(heap)
        merged_node = Node(None, left_node.freq + right_node.freq)
        merged_node.left = left_node
        merged_node.right = right_node
        heapq.heappush(heap, merged_node)

    return heap[0]


def generate_codes(root, prev_code="", codes={}):
    if root is not None:
        if root.char is not None:
            codes[root.char] = prev_code
        generate_codes(root.left, prev_code + "0", codes)
        generate_codes(root.right, prev_code + "1", codes)


if __name__ == "__main__":
    char_freq_tuples = [('a', 5), ('b', 9), ('c', 12), ('d', 13), ('e', 16), ('f', 45)]

    huffman_tree = build_tree(char_freq_tuples)

    huffman_codes = {}
    generate_codes(huffman_tree, "", huffman_codes)

    for char, code in huffman_codes.items():
        print(f"Character: {char}, Huffman Code: {code}")
