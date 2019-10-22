class list(list):
    def __lt__(self,other):
        return sum(self)>sum(other)
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, ([u, v] for u in nums1 for v in nums2),key = sum)