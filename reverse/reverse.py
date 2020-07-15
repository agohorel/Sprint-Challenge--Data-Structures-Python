class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return f"{self.value}"

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return f"{self.head}"

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def display(self):
        cur = self.head
        arr = []
        while cur:
            arr.append(cur)
            cur = cur.next_node
        print(arr)

    def reverse_list(self, node, prev):
        """ recursive version """
        if node is None or node.next_node is None:
            self.head = node # reset head if base case is hit
            return 

        val = self.reverse_list(node.next_node, node) # recurse to next node in list
        node.next_node.next_node = node # reverse pointer 
        node.next_node = prev # cancel out pointer going the other way, works w/ null or prev?
        return val

        """ iterative version """
        # cur = node
        # prv = prev

        # while cur:
        #     nxt = cur.next_node # temp var to store next before we alter it's ref in the following lines
        #     cur.next_node = prv # swap next with prev
        #     prv = cur # set prev to current
        #     cur = nxt # set cur to next (advance loop)
        # self.head = prv # don't forget to re-set the head!


ll = LinkedList()

ll.add_to_head(1)
ll.add_to_head(2)
ll.add_to_head(3)

ll.display()

ll.reverse_list(ll.head, None)

ll.display()