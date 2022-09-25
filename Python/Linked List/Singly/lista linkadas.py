from typing import Type
# class linkedListNode:
#
#     def __init__(self,value,nextNode=None):
#
#         self.value = value
#         self.nextNode = nextNode
#
#
# node1 = linkedListNode ( " 3 " )
# node2 = linkedListNode ( " 7 " )
# node3 = linkedListNode ( " 10 " )
# node4 = linkedListNode ( " 77 " )
#
# node1.nextNode = node2 # node1 - > node2 , " 3 " - > " 17 "
# node2.nextNode = node3 # node2 - > node3 " 7 " - > " 10 "
# node3.nextNode = node4
#
#
# currentNode = node1
# while True :
#     print (currentNode.value, '->')
#     if currentNode . nextNode is None :
#        print (" None ")
#        break
#
#     currentNode = currentNode.nextNode


class linkedListNode:

    def __init__(self,value,nextNode=None):

        self.value = value
        self.nextNode = nextNode

class linkedList:

    def __init__(self,head=None):
        self.head= head


    def insert(self,value):

        node = linkedListNode(value)
        if self.head == None:
            self.head = node
            return

        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

    def printLinkedList(self):

        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, " - > ",)
            currentNode = currentNode.nextNode
        print(" None ")


ll = linkedList ( )
ll.printLinkedList ( )
ll. insert ( " 3 " )
ll.printLinkedList ( )
ll.insert ( " 44 " )
ll.printLinkedList ( )
ll.insert ( " 55 " )
ll.printLinkedList( )
