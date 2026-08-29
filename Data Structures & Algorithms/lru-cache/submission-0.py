class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.d:

            node = self.d[key]
            node.prev.next = node.next
            node.next.prev = node.prev

            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node

            return node.val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            old = self.d[key]
            old.prev.next = old.next
            old.next.prev = old.prev
        
        node = Node(key, value)
        self.d[key] = node

        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

        if len(self.d) > self.cap:
            toRemove = self.head.next
            toRemove.next.prev = self.head
            self.head.next = toRemove.next
            del self.d[toRemove.key]





        
