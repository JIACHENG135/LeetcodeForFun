# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def __lt__(self,other):
    return self.val<other.val
ListNode.__lt__ = __lt__
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = []
        for n in lists:
            if n:
                heapq.heappush(h,n)
        
        dummy = head = ListNode(1)
        while h:
            cur = heapq.heappop(h)
            head.next = cur
            head = head.next
            if cur.next:
                heapq.heappush(h,cur.next)
        return dummy.next