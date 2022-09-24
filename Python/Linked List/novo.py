class Node:

    def __init__(self, valor):
        self.__value = valor
        self.__next = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, valor):
        self.__value = valor

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node):
        self.__next = node


class LinkedList:

    def __init__(self):
        self.head = None

    def add_begining(self, data):
        """  Adiciona no comeco da lista  """

        node = Node(data)
        node.next = self.head
        self.head = node

    def insert(self, data):

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        currentnode = self.head

        while currentnode.next is not None:
            currentnode = currentnode.next

        currentnode.next = new_node

    def add_after_node(self, data, node_value):

        current_node = self.head
        while current_node is not None:
            if current_node.value == node_value:
                break
            current_node = current_node.next

        if current_node is None:
            print('Node is not present in the Linled List')
        else:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node

    def find(self, valor):

        currentnode = self.head

        while currentnode is not None:
            if currentnode.value == valor:
                break
            currentnode = currentnode.next

        if currentnode is None:
            return 'Lista Vazia ou valor nao esta na lista'
        else:
            return currentnode

    def printlist(self):

        if self.head is None:
            return 'Lista Vazia'
        else:
            n = self.head
            while n is not None:
                print(n.value, '-->', end=' ')
                n = n.next


linked = LinkedList()

linked.insert(10)
linked.insert(20)
linked.insert(30)
linked.add_begining(50)
linked.add_begining(100)
linked.printlist()
# print('')
# linked.add_after_node(60,10)
#
# linked.printList()
