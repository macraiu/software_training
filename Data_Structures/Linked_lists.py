
""" 
Lined lists:
- each element called NODE
- each NODE:
--data
--next element

Head
3| -> 1| -> 4| -> 10| -> None

Queue:
First-in/First-Out
You append at the end and retrieve from the front

Stack:
Last-in/First-out
Last element inserted is the first to be retrieved

Because of the way you insert and retrieve elemtns from these last, Linked List are one of the most
convenient way of implement these data structures.

Deque:
Double-ended queue - Linked list that you can acess, insert and remove elements in O(1) time complexity.

from collections import deque
llist = deque('abcde')
llist.append('f')
llist.pop()
llist.appendleft('z')
llist.popleft()

For Queue:
llist.append('')
llist.popleft()

For Stack:
llist.appendleft()
llist.popleft()

Or simply with list:
list.append()
list.pop()

Next: See implementation of Linked List:
 """

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

llist = LinkedList(['x','y','z'])
print(llist)

first_node = Node('a')
llist.head = first_node

print(llist)
    
second_node = Node('b')
third_node = Node('c')

first_node.next = second_node
second_node.next = third_node

print(llist)



