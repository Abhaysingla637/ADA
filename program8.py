import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoder:
    def __init__(self):
        self.root = None
        self.codes = {}

    def build_tree(self, frequencies):
        heap = []

        for char, freq in frequencies.items():
            heapq.heappush(heap, Node(char, freq))

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            new = Node(None, left.freq + right.freq)
            new.left = left
            new.right = right

            heapq.heappush(heap, new)

        self.root = heap[0]
        return self.root

    def generate_codes(self):
        def traverse(node, code):
            if node is None:
                return

            if node.char is not None:
                self.codes[node.char] = code or "0"
                return

            traverse(node.left, code + "0")
            traverse(node.right, code + "1")

        self.codes = {}
        traverse(self.root, "")
        return self.codes


# Main Program

freq = {'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}

h = HuffmanCoder()
h.build_tree(freq)

print("Huffman Codes:")
print(h.generate_codes())
