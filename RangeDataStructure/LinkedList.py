class Node(object):
    """A Node of linked list

    ...

    Attributes
    ----------

    data : 
    Value stored at node
    
    next :
    Pointer to next node

    prev : 
    Pointer to prev node

    """
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList(object):
    """A quick implementation of DLL datastructure

    ...

    Attributes
    ----------

    head : 
    Pointer to head of list
    
    tail :
    Pointer to tail of list

    length : int
    Length of list
    
    Methods
    -------

    insert_front(data):
    Adds new node to head of list

    insert_back(data):
    Adds new node to tail of list

    insert_next(node, data):
    Adds new node as the next element to provided node

    delete(node):
    Removes node from list

    get_all_data():
    Returns data in list as a python List object

    """
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        self.length = 0

    def insert_front(self, data):
        new_node = Node(data, self.head)
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.length += 1

    def insert_back(self, data):
        if self.tail:
            self.tail.next = Node(data, None, self.tail)
            self.tail = self.tail.next
        else:
            self.head = self.tail = Node(data)
        self.length += 1

    def insert_at_node(self, node, data):
        if node == self.head:
            self.insert_front(data)
        elif node == None:
            self.insert_back(data)
        elif node:
            new_node = Node(data, node, node.prev)
            node.prev = new_node
            new_node.prev.next = new_node

    def delete(self, node):
        if(node == self.head):
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif(node == self.tail):
            if self.tail.prev:
                self.tail = self.tail.prev
            else:
                self.head = None
            self.tail.next = None
        else:
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev

        self.length -= 1

    def get_all_data(self):
        data = []
        current = self.head
        while current is not None:
            data.append(current.data)
            current = current.next
        return data


