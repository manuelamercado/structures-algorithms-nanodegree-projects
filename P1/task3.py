"""
Overview - Data Compression
In general, a data compression algorithm reduces the amount of memory (bits) required to represent a message (data). The compressed data, in turn, helps to reduce the transmission time from a sender to receiver. The sender encodes the data, and the receiver decodes the encoded data. As part of this problem, you have to implement the logic for both encoding and decoding.

A data compression algorithm could be either lossy or lossless, meaning that when compressing the data, there is a loss (lossy) or no loss (lossless) of information. The Huffman Coding is a lossless data compression algorithm. Let us understand the two phases - encoding and decoding with the help of an example.

A. Huffman Encoding
Assume that we have a string message AAAAAAABBBCCCCCCCDDEEEEEE comprising of 25 characters to be encoded. The string message can be an unsorted one as well. We will have two phases in encoding - building the Huffman tree (a binary tree), and generating the encoded data. The following steps illustrate the Huffman encoding:

Phase I - Build the Huffman Tree
A Huffman tree is built in a bottom-up approach.

First, determine the frequency of each character in the message. In our example, the following table presents the frequency of each character.
(Unique) Character	Frequency
A	7
B	3
C	7
D	2
E	6
Each row in the table above can be represented as a node having a character, frequency, left child, and right child. In the next step, we will repeatedly require to pop-out the node having the lowest frequency. Therefore, build and sort a list of nodes in the order lowest to highest frequencies. Remember that a list preserves the order of elements in which they are appended.

We would need our list to work as a priority queue, where a node that has lower frequency should have a higher priority to be popped-out. The following snapshot will help you visualize the example considered above:


Can you come up with other data structures to create a priority queue? How about using a min-heap instead of a list? You are free to choose from anyone.

Pop-out two nodes with the minimum frequency from the priority queue created in the above step.
Create a new node with a frequency equal to the sum of the two nodes picked in the above step. This new node would become an internal node in the Huffman tree, and the two nodes would become the children. The lower frequency node becomes a left child, and the higher frequency node becomes the right child. Reinsert the newly created node back into the priority queue.

Do you think that this reinsertion requires the sorting of priority queue again? If yes, then a min-heap could be a better choice due to the lower complexity of sorting the elements, every time there is an insertion.

Repeat steps #3 and #4 until there is a single element left in the priority queue. The snapshots below present the building of a Huffman tree.


For each node, in the Huffman tree, assign a bit 0 for left child and a 1 for right child. See the final Huffman tree for our example:

Phase II - Generate the Encoded Data
Based on the Huffman tree, generate unique binary code for each character of our string message. For this purpose, you'd have to traverse the path from root to the leaf node.
(Unique) Character	Frequency	Huffman Code
D	2	000
B	3	001
E	6	01
A	7	10
C	7	11
Points to Notice

Notice that the whole code for any character is not a prefix of any other code. Hence, the Huffman code is called a Prefix code.
Notice that the binary code is shorter for the more frequent character, and vice-versa.
The Huffman code is generated in such a way that the entire string message would now require a much lesser amount of memory in binary form.
Notice that each node present in the original priority queue has become a leaf node in the final Huffman tree.
This way, our encoded data would be 1010101010101000100100111111111111111000000010101010101

B. Huffman Decoding
Once we have the encoded data, and the (pointer to the root of) Huffman tree, we can easily decode the encoded data using the following steps:

Declare a blank decoded string
Pick a bit from the encoded data, traversing from left to right.
Start traversing the Huffman tree from the root.
If the current bit of encoded data is 0, move to the left child, else move to the right child of the tree if the current bit is 1.
If a leaf node is encountered, append the (alphabetical) character of the leaf node to the decoded string.
Repeat steps #2 and #3 until the encoded data is completely traversed.
You will have to implement the logic for both encoding and decoding in the following template. Also, you will need to create the sizing schemas to present a summary.

Visualization Resource
Check this website to visualize the Huffman encoding for any string message - Huffman Visualization! https://people.ok.ubc.ca/ylucet/DS/Huffman.html
https://classroom.udacity.com/nanodegrees/nd256-ent/parts/3e1f628f-e44f-4278-9cce-77bfa29f7ea2/modules/19cbca3b-396e-42c0-bfe2-5f92899e35fd/lessons/e6a27355-3fa2-43f1-936e-112c0a097f62/concepts/b97f3d67-ed9e-4759-8841-d13096f5cdd7
"""
from hashlib import new
import sys


class Node:
    def __init__(self, char, freq, left=None, right=None, binary_value=''):
        self.char = char
        self.left = left
        self.right = right
        self.binary_value = binary_value
        self.freq = freq


class Tree(object):
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root


def print_nodes(node, val=''):
    new_value = val + str(node.binary_value)

    if(node.left):
        print_nodes(node.left, new_value)
    if(node.right):
        print_nodes(node.right, new_value)

    if(not node.left and not node.right):
        print(f"{node.char} -> {new_value}")


def pre_order(tree):
    visit_order = list()
    root = tree.get_root()

    def tranverse(node):
        if node:
            visit_order.append(node.get_value())

            tranverse(node.get_left_child())

            tranverse(node.get_right_child())
            
    tranverse(root)
    
    return visit_order


def get_encoded_data(node, data):
    new_value = []

    def tranverse(node):
        if node:
            new_value.append(str(node.binary_value))

            if(node.left and data in node.left.char):
                tranverse(node.left)
            if(node.right and data in node.right.char):
                tranverse(node.right)

    tranverse(node)
    result = ''
    return result.join(new_value)


def huffman_encoding(data):
    quantities = {}
    tree = Tree()

    if not data:
        return "", None

    for character in data:
        if character not in quantities:
            quantities[character] = 1
        else:
            quantities[character] += 1

    nodes = []

    for value in quantities:
        nodes.append(Node(value, quantities[value]))

    if len(nodes) == 1:
        nodes[0].binary_value = 0

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
    
        left = nodes[0]
        right = nodes[1]

        left.binary_value = 0
        right.binary_value = 1

        parent = Node(left.char + right.char, left.freq + right.freq, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(parent)

    print_nodes(nodes[0])
    tree.root = nodes[0]

    encoded_data = ''
    for character in data:
        encoded_data += get_encoded_data(tree.root, character)

    return encoded_data, tree


def huffman_decoding(data, tree):
    if not data:
        return ""

    decoded_data = ''
    node = tree.root
    bit = 0

    for index in range(len(data) + 1):
        if index < len(data):
            bit = int(data[index])

        if node.left is None and node.right is None and len(decoded_data) < len(data):
            decoded_data += node.char
            node = tree.root

        if node.left and bit == 0 and bit == node.left.binary_value:
            node = node.left
        elif node.right and bit == 1 and bit == node.right.binary_value:
            node = node.right

    return decoded_data

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))  # 0110111011111100111000001010110000100011010011110111111010101011001010

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    a_great_sentence = "AAAAAAAAAAAAAAA"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))  #000000000000000

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    a_great_sentence = ""

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(0 if not encoded_data else sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
