# A linked list is a sequence of data elements, which are connected together via links. Each data element contains a
# connection to
# another data element in form of a pointer. Python does not have linked lists in its standard library.
#
# See code below to understand how to create a node class and use this to create a singly linked lists.
# In this type of data structure there is only one link between any two data elements.

class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3