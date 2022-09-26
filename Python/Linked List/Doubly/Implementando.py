class Node:

    def __init__(self,value):

        self.value = value
        self.next = None
        self.previous = None


class doublyLL:

    def __init__(self):

        self.head = None

    def empty_insert(self,data):

        if self.head is None:
            new_node = Node(data)
            self.head = new_node

        else:
            print('Liked List is not empty')


    def begin_insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def end_insert(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            current_node = self.head

            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node
            new_node.previous = current_node

    def print_ll(self):
        if self.head is None:
            print('List empty')

        else:
            current_node = self.head
            while current_node is not None:

                print(current_node.value,'-->',end=' ')
                current_node = current_node.next

    def print_ll_reverser(self):
        if self.head is None:
            print('List empty')
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            while current_node is not None:
                print(current_node.value, '-->', end=' ')
                current_node = current_node.previous


linked = doublyLL()

linked.empty_insert(10)
linked.begin_insert(50)
linked.end_insert(20)
linked.print_ll_reverser()
