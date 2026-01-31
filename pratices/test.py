class Node():
    def __init__(self, data, next=None, prev= None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_begining(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node

        else:
            node.next = self.head
            self.head = node

    def insert_end(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node


    def insert_at(self, data, index):
        node = Node(data)
        if index == 0:
            node.next = self.head
            self.head = node
            return

        current= self.head
        count = 0

        while current is not None:
            if count == index -1:
                node.next = current.next
                current.next = node
                return

            current = current.next
            count += 1

    def print(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next





ll = LinkedList()
ll.insert_begining('a')
ll.insert_begining('b')
ll.insert_begining('c')

ll.print()
print("\n")

ll.insert_at('f', 2)
ll.print()

