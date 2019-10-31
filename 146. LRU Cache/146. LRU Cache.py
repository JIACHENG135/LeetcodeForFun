class ListNode:
    def __init__(self,key=0,value=0):
        self.val = value
        self.key = key
        self.next = None
        self.prev = None
    
class LRUCache:
    def _add_node(self,node):
        node.next = self.head.next
        node.prev = self.head
        
        self.head.next.prev = node
        self.head.next = node
    
    def _del_node(self,node):
        node.next.prev,node.prev.next = node.prev,node.next
    
    def _move_to_head(self,node):
        self._del_node(node)
        self._add_node(node)
        
    def _pop_tail(self):
        self.act -= 1
        res = self.tail.prev
        self.tail.prev = res.prev
        res.prev.next = self.tail
        return res
    
    def __init__(self, capacity: int):
        self.size = capacity
        self.act = 0
        self.head,self.tail = ListNode(),ListNode()
        self.head.next,self.head.prev = self.tail,self.tail
        self.tail.next,self.tail.prev = self.head,self.head
        self.m = {}
    def get(self, key: int) -> int:
        if key in self.m:
            self._move_to_head(self.m[key])
            return self.m[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        node = self.m.get(key,None)
        
        if not node:
            self.act += 1
            new = ListNode(key,value)
            self._add_node(new)
            self.m[key] = new
        else:
            node.val = value
            self._move_to_head(node)
        if self.act>self.size:
            res = self._pop_tail()
            del self.m[res.key]