class TreeNode:
    def __init__(self,val):
        self.val = val
        self.parent = None
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        m = collections.defaultdict(str)
        for p,*c in regions:
            for city in c:
                m[city] = p
        
        path1 = [region1]
        while m[region1]:
            path1.append(m[region1])
            region1 = m[region1]
        
        
        path2 = [region2]
        while m[region2]:
            path2.append(m[region2])
            region2 = m[region2]
        path1 = path1[::-1]
        path2 = path2[::-1]
        # print(path1,path2)
        for i in range(min(len(path1),len(path2))):
            if path1[i]!=path2[i]:
                break
            prev = path1[i]
        return prev
        