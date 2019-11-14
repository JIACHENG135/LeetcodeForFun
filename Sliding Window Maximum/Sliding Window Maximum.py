class ListNode:
    def __init__(self,val,next= None,prev = None):
        self.val = val
        self.next = next
        self.prev = prev
class Dlist:
    def __init__(self,capacity):
        self.head = ListNode(float("inf"))
        self.tail = ListNode(float("inf"))
        self.head.next = self.tail
        self.tail.prev = self.head


    def popleft(self):
        head = self.head.next
        self.head.next = head.next
        head.next.prev = self.head

        return head.val
    
    def append(self,val):
        newNode = ListNode(val)
        prev = self.tail.prev
        while prev.val<val:
            prev = prev.prev
        prev.next = newNode
        newNode.prev = prev
        newNode.next = self.tail
        self.tail.prev = newNode

        

    def top(self):
        return self.head.next.val
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        deque = Dlist(k)
        for i in range(k):
            deque.append(nums[i])
        ans = [deque.top()]
        for i in range(k,len(nums)):
            left = nums[i-k]
            if deque.top()==left:
                deque.popleft()
            deque.append(nums[i])
            ans.append(deque.top())
        return ans
        
        