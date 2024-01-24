#!/usr/bin/python3

"""class, Node, that defines a node of a singly linked list"""


class Node:
    """Class definition"""
    def __init__(self, data, next_node=None):
        """data + next_node definition"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """property to retrieve it"""
        return self.__data

    @data.setter
    def data(self, value):
        """property setter to set it"""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """property to retrieve it"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """property setter to set it"""
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node


class SingleLinkedList:
    """Class definition"""
    def __init__(self):
        """private instance attribute"""
        self.__head = None

    def sorted_insert(self, value):
        """insert Node into correct sorted position in the list"""
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head

        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """print the entire list to stdout"""
        result = ''
        current = self.__head
        while current is not None:
            result += str(current.data) + '\n'
            current = current.next_node
        return result
