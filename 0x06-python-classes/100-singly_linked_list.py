#!/usr/bin/python3
""" Node class """


class Node:
    """ Node class that defines a node
    Attributes:
        prmData: value of the node
        prmNextNode: next node
    """
    __data = 0
    __next_node = None

    def __init__(self, prmData, prmNextNode=None):
        self.data = prmData
        self.next_node = prmNextNode

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, prmData):
        if (not isinstance(prmData, int)):
            raise TypeError("data must be an integer")
        self.__data = prmData

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, prmNextNode=None):
        if (prmNextNode is not None and not isinstance(prmNextNode, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = prmNextNode
""" SinglyLinkedList class """


class SinglyLinkedList:
    """ SinglyLinkedList class that defines a singly list """
    __head = None

    def __init__(self):
        pass

    def __str__(self):
        head = self.__head
        result = ""

        while (head is not None):
            result += str(head.data)
            if (head.next_node is not None):
                result += '\n'
            head = head.next_node
        return result

    def sorted_insert(self, prmValue):
        new = Node(prmValue)
        head = self.__head

        while (
            head is not None and head.next_node is not None and
            head.next_node.data < new.data
        ):
            head = head.next_node

        if head is None:
            self.__head = new
        else:
            new.next_node = head.next_node
            head.next_node = new
            if (head.data > new.data):
                tmp = new.data
                new.data = head.data
                head.data = tmp
