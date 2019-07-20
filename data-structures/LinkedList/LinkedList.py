"""
Problem:
    - Given a linked list of nodes representing a binary number,
    convert the number to base 10.
    - Implement a simple linked list.
"""

class Node:
   def __init__(self, value):
    self.node_value = value
    self.nextNode = None
 
class LinkedList:
    def __init__(self, value_list):
        self.head = None
        curr = None

        for v in value_list:
            if curr == None:
                self.head = Node(v)
                curr = self.head
            else:
                curr.nextNode = Node(v)
                curr = curr.nextNode

def convertToBase10(my_list):
    curr = my_list.head
    summation = 0

    while curr != None:
        summation = (summation << 1) + curr.node_value
        curr = curr.nextNode

    return summation
