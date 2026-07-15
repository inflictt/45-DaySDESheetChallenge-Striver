class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


# so made the ds / node for my usage using hashmap and dll
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = dict()
        self.left, self.right = Node(0, 0), Node(0, 0)  # node created
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):  # ths is lru
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):  # this is mru
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:  # then update it to mru and return if not return -1
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val  # so now value is return
        return -1

    def put(self, key: int, value: int) -> None:
        if (
            key in self.cache
        ):  # if in there remove first then append it again with insert
            self.remove(self.cache[key])
            self.cache[key] = Node(
                key, value
            )  # this is new node creatded now insertion next
            self.insert(self.cache[key])
        else:
            if self.cap != len(self.cache):
                self.cache[key] = Node(key, value)  # node created
                self.insert(self.cache[key])  # node inserted to mru as recerntly added
            else:  # capacity is full
                lru = self.left.next  # get teh least recently used
                self.remove(lru)  # removed rthe lru
                del self.cache[lru.key]  # deleted tehatg
                newNode = Node(key, value)
                self.cache[key] = newNode
                self.insert(newNode)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
