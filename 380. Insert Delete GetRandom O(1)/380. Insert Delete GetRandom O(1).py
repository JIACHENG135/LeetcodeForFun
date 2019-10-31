class ListNode:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head,self.tail = ListNode(1),ListNode(1)
        self.head.next,self.tail.prev = self.tail,self.head
        self.m = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.m:
            return False
        new = ListNode(val)
        next_node = self.head.next
        self.head.next,new.prev = new,self.head
        next_node.prev,new.next = new,next_node
        self.m[val] = new
        return True
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.m:
            return False
        node = self.m[val]
        
        prev,nxt = node.prev,node.next
        prev.next,nxt.prev = nxt,prev
        del self.m[val]
        return True
        
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        keys = list(self.m.keys())
        m = random.randint(0,len(keys)-1)
        return self.m[keys[m]].val