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

    def before_insert(self,value,node):

        new_node = Node(value)

        if self.head is None:
            print('The list is empty')
            return

        current_node = self.head

        while current_node is not None:
            if current_node.value == node:
                break
            current_node = current_node.next

        if current_node is None:
            print('Given Node is not present in the list')
        else:
            new_node.next = current_node
            new_node.previous = current_node.previous
            current_node.previous.next = new_node
            current_node.previous = new_node

    def after_insert(self,value,node):

        new_node = Node(value)

        if self.head is None:
            print('The list is empty')
            return

        current_node = self.head

        while current_node is not None:
            if current_node.value == node:
                break

            current_node = current_node.next

        if current_node is None:
            print('Given Node is not present in the list')
        else:
            new_node.next = current_node.next
            new_node.previous = current_node

            if current_node.next is not None:
                current_node.next.previous = new_node

            current_node.next = new_node


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

    def find(self,node):

        if self.head is None:
            print('List empty')

        current_node = self.head

        while self.head is not None:
            if current_node.value == node:
                break
            current_node = current_node.next

        if current_node is None:
            print("Node not found")
            return

        self.print_node_status(current_node)

        return current_node
    def print_node_status(self,node):

        try:
            next = node.next.value
        except AttributeError:
            next = 'None'
        try:
            previous = node.previous.value
        except AttributeError:
            previous = 'None'

        print(f'next:{previous}, prev:{next}')

linked = doublyLL()

linked.empty_insert(10)
linked.begin_insert(50)
linked.end_insert(20)
linked.before_insert(100,10)
linked.before_insert(200,100)
linked.after_insert(60,200)
a = linked.find(20)
linked.print_ll()
