"""
Blockchain
A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.


We can break the blockchain down into three main parts.

First is the information hash:
"""
import hashlib
import datetime


"""
We do this for the information we want to store in the block chain such as transaction time, data, and information like the previous chain.

The next main component is the block on the blockchain:
"""


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data, timestamp)
        self.next = None

    def __repr__(self):
        return (
            str(self.timestamp) +
            " | " +
            str(self.data) +
            " | previous -> " +
            str(self.previous_hash) +
            " | self -> " +
            str(self.hash)
        )

    def calc_hash(self, data, timestamp):
        if not data:
            return

        sha = hashlib.sha256()
        hash_str = data.encode('utf-8') + str(timestamp).encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()


"""
Above is an example of attributes you could find in a Block class.
Finally you need to link all of this together in a block chain, which you will be doing by implementing it in a linked list. All of this will help you build up to a simple but full blockchain implementation!
"""


class BlockChain:
    def __init__(self):
        self.head = None

    def preappend(self, data, timestamp=None):
        if not data:
            return

        head = self.head
        timestamp = datetime.datetime.utcnow() if not timestamp else timestamp

        if head is None:
            previous_hash = 0
            head = Block(timestamp, data, previous_hash)
            self.head = head
            return

        node = Block(timestamp, data, head.hash)
        node.next = head
        self.head = node
    
    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node)
            node = node.next
        return out


# Test Case 1
bl = BlockChain()
data1 = "First Blockchain block"
data2 = "Second Blockchain block"
data3 = "Third Blockchain block"
bl.preappend(data1)
bl.preappend(data2)
bl.preappend(data3)
print(bl.to_list(), '\n')  # prints block chain
# Test Case 2
bl1 = BlockChain()
bl1.preappend("")
bl1.preappend("")
print(bl1.to_list(), '\n')  # prints empty block chain as there was no data passed
# Test Case 3
bl2 = BlockChain()
bl2.preappend(None)
bl2.preappend(None)
print(bl2.to_list(), '\n')  # prints empty block chain as there was no data passed
# Test Case 4 Same timestamp
timestamp = datetime.datetime.utcnow()
bl3 = BlockChain()
bl3.preappend(data1, timestamp)
bl3.preappend(data2, timestamp)
bl3.preappend(data3)
print(bl3.to_list(), '\n')  # prints block chain
