class LRUCache(object):
    def __init__(self, MAX_SIZE):
        self.size = 0
        self.MAX_SIZE = MAX_SIZE
        self.query_to_node = dict()
        self.linked_list = LinkedList()

    def add(self, query, results):
        """Add the input query-result pair to the cache.
        
        Updating a node moves it to the front of the LRU list. If a new node is
        constructed when the cache is full, the least-recently-used entry is removed, and
        the new node is added to the front of the list.
        """
        node = self.query_to_node.get(query)
        if node:
            node.results = results
            self.linked_list.move(node)
        else:
            if self.size == self.MAX_SIZE:
                del self.query_to_node[self.linked_list.tail.previous.query]
                self.linked_list.remove(self.linked_list.tail.previous)
            else:
                self.size += 1

            new_node = Node(query, results)
            self.linked_list.add(new_node)
            self.query_to_node[query] = new_node

    def get(self, query):
        """Get the result associated with the input query from the cache.
        
        Accessing a node moves it to the front of the LRU list.
        """
        node = self.query_to_node.get(query)
        if not node:
            return None
        self.linked_list.move(node)
        return node.results

class Node(object):
    def __init__(self, query=None, results=None):
        self.query = query
        self.results = results
        self.previous = None
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.previous = self.head

    def move(self, node):
        self.remove(node)
        self.add(node)

    def add(self, node):
        node.next = self.head.next
        node.previous = self.head
        self.head.next.previous = node
        self.head.next = node

    def remove(self, node):
        node.previous.next = node.next
        node.next.previous = node.previous
