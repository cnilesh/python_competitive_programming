class Node():
    def __init__(self, value):
        self._next = None
        self._value = value

    def printAll(self):
        print('Printing linkedlist')
        while self != None:
            print(self._value)
            self = self._next
    
    def removeNode(self, node):
        while self != None:
            if self._next == node:
                self._next = self._next._next
                self._next._next = None
                break
            self = self._next
                
    
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1._next = node2
node2._next = node3
node1.printAll()
node1.removeNode(node2)
node1.printAll()