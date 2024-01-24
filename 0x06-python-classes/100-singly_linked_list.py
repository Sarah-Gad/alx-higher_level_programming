#!/usr/bin/python3

""" This is a definition of a class"""


class Node:
    """ this defines a node"""

    def __init__(self, data, next_node=None):
        """ initialise the node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gets the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """assogn the data of the node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ gets the nest node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """assign the nesxt node"""
        if not isinstance(value, (Node, type(None))):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    class SinglyLinkedList:
        """ this is the singly linked list"""
        def __init__(self):
            """ start the singly linked list"""
            self.__head = None

        def __str__(self):
            """ the string of the list"""
            string = ""
            start = self.__head
            while start:
                if start is not self.__head:
                    string += '\n'
                string += str(start.data)
                start = start.next_node
            return string

        def sorted_insert(self, value):
            """ insert the new nodde"""
            new = Node(value)
            if not self.__head:
                self.__head = new
                return
            prev = None
            temp = self.__head
            while temp:
                if value < temp.data:
                    break
                prev = temp
                temp = temp.next_node
            if prev:
                prev.next_node = new
            else:
                self.__head = new
            new.next_node = temp
