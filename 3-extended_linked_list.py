# Written by **** for COMP9021

from linked_list import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        copy = self.duplicate()
        for k in range(len(self)):
            self.delete_value(self.value_at(0))
        min = copy.value_at(0)
        min_index = 0
        length = len(copy)
        for i in range(length):
            if copy.value_at(i) < min:
                min = copy.value_at(i)
                min_index = i
        odd_index = min_index -1
        self.head = Node(min)
        odd_node = self.head
        i = 0
        for j in range(length//2+1):
            if i < length-1:
                if odd_index >= 0 and odd_index < length:
                    even_node = Node(copy.value_at(odd_index))
                    even_index = odd_index +3
                else:
                    even_node = Node(copy.value_at(length + odd_index))
                    even_index = length + odd_index + 3
                odd_node.next_node = even_node
                i += 1
            if i < length-1:
                if even_index >= 0 and even_index < length:
                    odd_node = Node(copy.value_at(even_index))
                    odd_index = even_index - 1
                else:
                    odd_node = Node(copy.value_at(-length + even_index))
                    odd_index = - length + even_index -1
                even_node.next_node = odd_node
                i += 1
        return self
    
    
