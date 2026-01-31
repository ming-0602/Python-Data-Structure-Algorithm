class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data   # store the data
        self.next = next   # pointer to next node
        self.prev = prev   # pointer to previous node


class LinkedList:
    def __init__(self):
        self.head = None   # first node
        self.tail = None   # last node

    def insert_at_beginning(self, data):
        # Create a new node
        node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            # Connect new node to current head
            node.next = self.head
            self.head.prev = node
            # Update head
            self.head = node

    def insert_at_end(self, data):
        # Create a new node
        node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            # Connect new node with current tail
            node.prev = self.tail
            self.tail.next = node
            # Update tail
            self.tail = node

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise ValueError("Index out of range")

        if index == 0:
            self.insert_at_beginning(data)
            return

        if index == self.get_length():
            self.insert_at_end(data)
            return

        # Traverse to index-1
        count = 0
        itr = self.head
        while itr is not None:
            if count == index - 1:
                node = Node(data)
                # Link new node
                node.next = itr.next
                node.prev = itr
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                return
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise ValueError("Index out of range")

        # Remove head
        if index == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
            return

        count = 0
        itr = self.head
        while itr is not None:
            if count == index:
                # Remove connections
                if itr.prev:
                    itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                else:
                    # If removing last node, update tail
                    self.tail = itr.prev
                return
            itr = itr.next
            count += 1

    def get_length(self):
        count = 0
        itr = self.head
        while itr is not None:
            count += 1
            itr = itr.next
        return count

    def print_forward(self):
        if self.head is None:
            print("LinkedList is empty")
            return

        itr = self.head
        string = ""
        while itr is not None:
            string += str(itr.data)
            if itr.next:
                string += " <-> "
            itr = itr.next
        print(string)

    def print_backward(self):
        if self.tail is None:
            print("LinkedList is empty")
            return

        itr = self.tail
        string = ""
        while itr is not None:
            string += str(itr.data)
            if itr.prev:
                string += " <-> "
            itr = itr.prev
        print(string)


if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_beginning("A")
    llist.insert_at_end("B")
    llist.insert_at_beginning("C")
    llist.insert_at_end("D")
    llist.print_forward()    # C <-> A <-> B <-> D

    llist.remove_at(3)       # remove D
    llist.print_forward()    # C <-> A <-> B

    llist.insert_at(2, "R")
    llist.print_forward()    # C <-> A <-> R <-> B

    llist.print_backward()   # B <-> R <-> A <-> C
