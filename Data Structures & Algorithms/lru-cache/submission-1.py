class Node:
    def __init__(self, key: int=0, value: int=0, nxt=None, prev=None):
        self.key = key
        self.value = value
        self.next = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        # Create doubly linked list with head / tail dummy nodes
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity
        self.cache = {}


    def get(self, key: int) -> int:
        
        if key in self.cache:
            node = self.cache[key]
            # Remove node and place at the end
            self.remove(node)
            self.insertEnd(node)
            return node.value
        return -1

        

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)

        if key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)
        
        self.insertEnd(node)
        self.cache[key] = node
        

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]

    
    def remove(self, node: Node) -> None:
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

        node.prev = None
        node.next = None

    def insertEnd(self, node: Node) -> None:
        prevNode = self.tail.prev

        prevNode.next = node
        self.tail.prev = node

        node.next = self.tail
        node.prev = prevNode

        
