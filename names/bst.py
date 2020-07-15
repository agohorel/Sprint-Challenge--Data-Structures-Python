"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.value}"

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # if no left node, insert
            if self.left == None:
                self.left = BSTNode(value)
            # otherwise recurse left until empty spot is found
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            # if target is less than value and nothing to the left, it's not in the tree
            if self.left == None:
                return False
            # recurse left, if it hits base case it'll return true otherwise ^^^
            return self.left.contains(target)
        else:
            if self.right == None:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        # if no right node, return value (would have to be max)
        if self.right == None:
            return self.value
        # else if there's a right node, recurse right
        else:
            return self.right.get_max()

    def iterative_max(self):
        current = self
        record = self.value
        while current != None:
            if current.value > record:
                record = current.value
            current = current.right
        return record

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        # run callback on each iteration
        fn(self.value)
        # if there's somewhere to travel right, recurse right
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    def iterative_for_each(self, fn):
        s = Stack()
        s.push(self)

        while len(s) > 0:
            current = s.pop()
            if current.right:
                s.push(current.right)
            if current.left:
                s.push(current.left)
            fn(current)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node:
            if node.left:
                node.left.in_order_print(node.left)
            print(node)
            if node.right:
                node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while len(q.storage) > 0:
            # pop off last item & save ref
            current = q.dequeue()
            print(current)
            # is there a left node? if so recurse left
            if current.left:
                q.enqueue(current.left)
            # is there a right node? if so recurse right
            if current.right:
                q.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()
        s.push(node)
        while len(s.storage) > 0:
            current = s.pop()
            print(current)
            if current.left:
                s.push(current.left)
            if current.right:
                s.push(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node)
            if node.left:
                node.left.pre_order_dft(node.left)
            if node.right:
                node.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT

    def post_order_dft(self, node):
        if node:
            if node.left:
                node.left.post_order_dft(node.left)
            if node.right:
                node.right.post_order_dft(node.right)
            print(node)


class Queue:
    def __init__(self):
        self.storage = list()

    def enqueue(self, value):
        self.storage.insert(0, value)

    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.pop()


class Stack:
    def __init__(self):
        self.storage = list()

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if len(self.storage) > 0:
            return self.storage.pop()
