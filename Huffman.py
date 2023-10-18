import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_tree(char_freq_disc):
    heap = [Node(char, freq) for char, freq in char_freq_disc.items()]
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


def decompress(code_table, text):
    current_word = ""
    output = ""

    for c in text:
        current_word = current_word + c

        if current_word in code_table:
            output = output + code_table[current_word]
            current_word = ""
    return output


def compress(text):
    output = ["", {}]
    char_freq_dict = {}
    code_table = {}

    for c in text:
        if c in char_freq_dict:
            char_freq_dict[c] = char_freq_dict[c] + 1
        else:
            char_freq_dict[c] = 1

    generate_codes(build_tree(char_freq_dict), "", code_table)
    print(code_table)
    output[1] = code_table

    for c in text:
        output[0] = output[0] + code_table[c]

    return output




