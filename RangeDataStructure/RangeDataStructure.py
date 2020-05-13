import LinkedList

class RangeCollection(object):
    """A data structure used to keep track of and manipulate ranges

    Notes:
    A doubly linked list implementation was chosed in order to optimize for additions to start and end of list
    and to optimize for time taken to delete ranges.

    The use of a python list would have O(N) for addition to the front which renders O(logN) search useless
    The same can be said for an AVL tree or BST

    A skip-list was considered for this application and would be perfect if only Runtime complexity is to be considered
    as it will provide O(logN) search as well as O(logN) insertion and deletion
    The drawback of a skip-list is the memory overhead of the structure as well as the added complexity
    Further analysis of the use case could be helpful in determining the most suitable data structure

    ...

    Attributes
    ----------

    rangeCollections : 
        A datastructure holding the ranges
    
    start : int
        The starting value of the range

    end : int
        The ending value of the range
    
    Methods
    -------

    Runtime Complexity O(1)
    isValidRange : range
        Accepts a range and returns true if valid and false otherwise
    
    Runtime Complexity O(N) due to complexity of search, however because of use of linkedlist addition in place is O(1)
    add(start,end):
        Add a new range to the datastructure.

    Runtime Complexity O(N) (linear search)
    findStartNode(start):
        Return pointer to node whose range < start

    Runtime Complexity O(1)
    isRangeContained(newRange,range)
        Returns True if newRange is a subset of range, False otherwise

    Runtime Complexity O(M) where M is the number of nodes to be merged after current node
    mergeAfterAdd(insertionPostionNode):
        Performs a merge of nodes if required after a node has been added

    Runtime Complexity O(N) due to complexity of search, however because of use of linkedlist deletion in place is O(1)
    delete(start,end):
        Removes given range from datastructure
        Return false if no deletion takes place
        Return true otherwise

    Runtime Complexity O(N)
    get(start,end):
        Returns list of ranges that intersect with the start and end values provided

    Runtime Complexity O(N)
    get_all():
        Function that returns the current state of the datastructure

    """
    def __init__(self):
        self.collection = LinkedList.LinkedList()

    def isValidRange(self, range):
        try:
            value = int(range[0])
            value = int(range[1])
        except ValueError:
            return False
        if(range[0] > range[1]):
            return False
        return True

    def findStartNode(self, start):
        if start > self.collection.tail.data[1] or self.isRangeContained([start,start], self.collection.tail.data):
            return  self.collection.tail.next

        curr = self.collection.head
        while curr:
            if curr.data[0] > start:
                return curr
            curr = curr.next
        return curr

    def isRangeContained(self, newRange, range):
        if newRange[0] > range[0] and newRange[1] < range[1]:
            return True
        return False

    def mergeAfterAdd(self, insertionPostionNode):
        nextNode = insertionPostionNode.next

        while nextNode and nextNode.data[0] <= insertionPostionNode.data[1]:
            insertionPostionNode.data[1] = nextNode.data[1]
            self.collection.delete(nextNode)
            nextNode = insertionPostionNode.next
        return True

    def add(self, start, end):
        range = [start, end]
        if not self.isValidRange(range):
            return False

        insertionPostionNode = self.collection.head

        if self.collection.length == 0:
            self.collection.insert_front(range)
            insertionPostionNode = None
        elif self.collection.head.data[0] >= start:
            self.collection.insert_front(range)
            insertionPostionNode = insertionPostionNode.prev
        elif self.collection.tail.data[1] < start:
            self.collection.insert_back(range)
            insertionPostionNode = self.collection.tail
        else:
            insertionPostionNode = self.findStartNode(start)
            if not self.isRangeContained(range, self.collection.head.data):
                self.collection.insert_at_node(insertionPostionNode,range)
                if insertionPostionNode == None:
                    insertionPostionNode = self.collection.tail.prev
                else:
                    insertionPostionNode = insertionPostionNode.prev
        if insertionPostionNode:
            self.mergeAfterAdd(insertionPostionNode)
        return True

    def delete(self, start, end):
        range = [start, end]
        if not self.isValidRange(range):
            return False

        # If list is already empty
        if self.collection.length == 0:
            return True

        # If out of range
        if self.collection.head.data[0] > end or self.collection.tail.data[1] < start:
            return True

        startNode = self.findStartNode(start)
        if not startNode:
            startNode = self.collection.tail     
        
        # If range to be deleted is subset of current range
        if self.isRangeContained(range, startNode.data):
            temp = [startNode.data[0], startNode.data[1]]
            temp[1] = start
            self.collection.insert_at_node(startNode, temp)
            startNode.data[0] = end            
            return True

        # If range needs to be truncated
        if startNode.data[1] > start and startNode.data[0] < start:
            startNode.data[1] = start
            startNode = startNode.next

        while startNode:
            if self.isRangeContained(startNode.data, range):
                self.collection.delete(startNode)
                startNode = startNode.next
            elif startNode.data[0] < end:
                    startNode.data[0] = end 
                    return True
        return True

    def get(self, start, end):
        range = [start, end]
        if not self.isValidRange(range) or not self.collection.head:
            return []

        retList = []
        startNode = self.findStartNode(start)

        if startNode.prev:
            if startNode.prev.data[1] > start:
                retList.append(startNode.prev.data)

        while startNode and startNode.data[1] <= end:
            if startNode.data[0] >= start and startNode.data[1] <= end:
                if startNode.data[1] >= start and startNode.data[1] <= end:
                    retList.append(startNode.data)
            startNode = startNode.next

        return retList

    def get_all(self):
        return self.collection.get_all_data()