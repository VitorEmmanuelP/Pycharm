class Node:

    def __init__(self, value):
        self.__value = value
        self.__next = None
        self.__previous = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, data):
        self.__value = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, data):
        self.__next = data

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, data):
        self.__previous = data


class doublyLL:

    def __init__(self):

        self.head = None

    def __empty_insert(self, data):

        new_node = Node(data)
        self.head = new_node

    def begin_insert(self, data):

        if self.head is None:
            self.__empty_insert(data)

        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def end_insert(self, data):

        if self.head is None:
            self.__empty_insert(data)

        else:
            new_node = Node(data)
            current_node = self.head

            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node
            new_node.previous = current_node

    def before_insert(self, value, node):

        new_node = Node(value)

        if self.head is None:
            print('The list is empty')
        else:

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

    def after_insert(self, value, node):

        new_node = Node(value)

        if self.head is None:
            print('The list is empty')
        else:
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

    def removing_head(self):

        if self.head is None:
            print('The list is empty')
            return
        if self.head.next is None:
            self.head = None
            print('List is empty after deleting the node!')
        else:
            self.head = self.head.next
            self.head.previous = None

    def removing_tail(self):

        if self.head is None:
            print('The list is empty')
            return
        if self.head.next is None:
            self.head = None
            print('List is empty after deleting the node!')

        else:
            current_node = self.head

            while current_node.next is not None:
                current_node = current_node.next

            current_node.previous.next = None
    def removing_middle(self, node):

        if self.head is None:
            print('The list is empty')
        else:
            current_node = self.head

            while current_node is not None:
                if current_node.value == node:
                    break
                current_node = current_node.next

            current_node.next.previous = current_node.previous
            current_node.previous.next = current_node.next

    def print_ll(self):
        if self.head is None:
            print('List empty')

        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.value, '-->', end=' ')
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

    def find(self, node):

        if self.head is None:
            print('List empty')

        current_node = self.head

        while current_node is not None:
            if current_node.value == node:
                break
            current_node = current_node.next

        if current_node is None:
            print("Node not found")
            return

        self.__print_node_status(current_node)

        return current_node

    def __print_node_status(self, node):

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

linked.begin_insert(10)
linked.begin_insert(50)
linked.end_insert(20)
linked.before_insert(100, 10)
linked.before_insert(200, 100)
linked.after_insert(60, 200)
linked.after_insert(600, 20)
linked.print_ll()
print('')
linked.removing_middle(60)
linked.print_ll()
print('')
linked.removing_tail()
linked.print_ll()
print('')
linked.removing_head()
linked.print_ll()
print('')