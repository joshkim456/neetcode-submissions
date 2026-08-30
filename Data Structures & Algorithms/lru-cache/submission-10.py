class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def remove(self, key):
        if key in self.d:
            toRemove = self.d[key]

            temp = toRemove.next
            toRemove.prev.next = temp
            toRemove.next.prev = toRemove.prev
            
            del self.d[key]

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}

        self.head = self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.d:

            toAdd = self.d[key]

            toAdd.prev.next = toAdd.next
            toAdd.next.prev = toAdd.prev

            toAdd.next = self.tail
            toAdd.prev = self.tail.prev
            self.tail.prev.next = toAdd
            self.tail.prev = toAdd

            return self.d[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.d:
            toAdd = self.d[key]

            toAdd.prev.next = toAdd.next
            toAdd.next.prev = toAdd.prev

            toAdd.next = self.tail
            toAdd.prev = self.tail.prev
            self.tail.prev.next = toAdd
            self.tail.prev = toAdd
            toAdd.val = value
        else:
            toAdd = Node(key, value)
            self.d[key] = toAdd

            toAdd.next = self.tail
            toAdd.prev = self.tail.prev
            self.tail.prev.next = toAdd
            self.tail.prev = toAdd
        
        if len(self.d) > self.cap:
            self.remove(self.head.next.key)







        
