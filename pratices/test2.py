class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def add_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node.next = self.head
            self.head.next = new_node
            self.head = new_node
            self.size += 1


    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def add_specific(self, data, location):
        new_node = Node(data)
        if self.head is None or location == 0:
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
            self.size += 1
            return

        index = 0
        itr = self.head
        while itr is not None and index < location -1:
            itr = itr.next
            index += 1


        new_node.next = itr.next
        new_node.prev = itr
        if itr.next:
            itr.next.prev = new_node
        itr.next = new_node

        if new_node.next is None:
            self.tail = new_node

        self.size += 1


    def remove_first(self):
        if self.head is None:
            return

        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1

    def remove_last(self):
        if self.head is None:
            return

        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1


    def print(self):
        itr = self.head
        while itr is not None:
            print(itr.data)
            itr = itr.next


    def contains(self, data):
        itr = self.head
        while itr is not None:
            if itr.data == data:
                return True

        return False


