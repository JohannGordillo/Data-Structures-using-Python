#!/usr/bin/env python3

"""
=============================================================================
>> Author:   Johann Gordillo
>> Email:    jgordillo@ciencias.unam.mx
>> Date:     07/28/2020
>> License:  MIT License https://opensource.org/licenses/MIT 
=============================================================================
Implementation of a Doubly Linked List.

Note: 
Since english is not my first language, if you find mispelled words
or another kind of grammatical errors, please help me fixing them :D
=============================================================================
"""

class Node(object):
    """Implementation of a Node."""
    def __init__(self, elem):
        """Constructor for the node.

        Args:
            elem (any): Element inside the node.
        """
        self.next = None
        self.previous = None
        self.element = elem

    def __str__(self):
        """String representation of the node.

        Returns:
            str: A string representation of the node.
        """
        return str(self.element)

    def __eq__(self, obj):
        if not isinstance(obj, Node):
            raise Exception("The given object is not a Node")
        return self.element == obj.element


class LinkedList(object):
    """Implementation of a Doubly Linked List.
    
    A linked list with N elements looks like this:
    Tail ←→ Node 2 ←→ ... ←→ Node n-1 ←→ Head
    """
    def __init__(self):     
        """Constructor for the linked list."""
        self.head = None
        self.tail = None
        self._length = 0

    def get_length(self):
        """Returns the length of the list.

        Returns:
            int: The length of the list.
        """
        return self._length

    def append(self, elem, beginning=False):
        """Adds an element to the list.

        Args:
            elem (any): The element of the new node of the list.
            beginning (bool, optional): If True, adds the element to
            the beginning of the list. Otherwise, adds it to the end. 
            Defaults to False.
        """
        new = Node(elem)
        if self.head is None:
            self.head = self.tail = new
        else:
            if beginning:  # Adding an element to the beginning of the list.
                aux = self.tail
                new.next = aux
                aux.previous = new
                self.tail = new
            else:  # Adding an element to the end of the list.
                aux = self.head
                new.previous = aux
                aux.next = new
                self.head = new
        self._length += 1

    def delete(self, beginning=False):
        """Deletes an element from the list.

        Args:
            beginning (bool, optional): If True, deletes the first
            element from the list. Otherwise, deletes the last. 
            Defaults to False.

        Raises:
            Exception: Raises an exception when the list is empty.
        """
        if self.head is None:
            raise Exception("The list is already empty.")

        if beginning:
            # Deletes the node at the beginning of the list (the tail).
            self.tail = self.tail.next
            self.tail.previous = None
        else:
            # Deletes the node at the end of the list (the head).
            self.head = self.head.previous
            self.head.next = None
        self._length -= 1

    def find(self, elem):
        """This method finds the index of a given element, if it
        is in the list.

        Time Complexity: O(n)

        Args:
            elem (any): The element that we want to find.

        Raises:
            ValueError: Raises an exception when the element is
            not in the list.

        Returns:
            int: The index of the given element in the list.
        """
        n = self.tail
        idx = 0
        while n is not None:
            if n.element == elem:
                return idx
            n = n.next
            idx += 1
        raise ValueError("The element is not in the list")

    def insert(self, elem, idx):
        """Inserts a given element in a given index.

        Args:
            elem (any): The element that we want to insert.
            idx (int): The index.

        Raises:
            Exception: Raises an exception when the index is not valid.
        """
        if idx > self._length or idx < 0:
            raise Exception("The index is not valid")
        
        if idx == 0:
            self.append(elem, beginning=True)
        elif idx == self._length:
            self.append(elem)
        else:
            new = Node(elem)
            n = self.tail
            for _ in range(idx - 1):
                n = n.next
            aux = n.next
            n.next = new
            new.previous = n
            new.next = aux
            self._length += 1

    def reverse(self):
        """Method for reversing the linked list.
        Warning: This action is destructive.
        """
        n = self.tail
        while n is not None:
            aux = n.next
            n.next = n.previous
            n.previous = aux
            n = n.previous
        aux = self.head
        self.head = self.tail
        self.tail = aux

    def __str__(self):
        """String representation of the linked list.

        Returns:
            str: A string representing the linked list.
        """
        s = str()
        n = self.tail
        for i in range(self._length - 1):
            if i % 10 == 0:
                s += "\n"
            s += str(n) + " ←→ "
            n = n.next
        s += str(n)
        return s

    def __eq__(self, obj):
        if not isinstance(obj, LinkedList):
            raise Exception("The given object is not a Linked List")
        if self._length != obj.get_length():
            return False
        n1 = self.tail
        n2 = obj.tail
        while n1 is not None:
            if n1 != n2:
                return False
            n1 = n1.next
            n2 = n2.next
        return True


def main():
    """Main function.
    Examples of how the implementation works.
    """
    # Creating two new linked lists.
    ll1 = LinkedList()
    ll2 = LinkedList()

    # Filling both lists with the same 100 elements.
    for x in range(1,101):
        ll1.append(x)
        ll2.append(x)
    
    # Printing the first list.
    print("\nLinked List:")
    print(ll1)

    # Let's see if they are both equal.
    print("\nAre the lists equal?", ll1 == ll2)  # True
    
    # Reversing the first list and then printing it.
    ll1.reverse()
    print("\nReversed Linked List:")
    print(ll1)

    # Let's see, again, if they are both equal.
    print("\nAre the lists equal?", ll1 == ll2)  # False


if __name__ == "__main__":
    main()
