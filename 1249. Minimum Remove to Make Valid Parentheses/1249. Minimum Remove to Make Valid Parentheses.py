class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = [l for l in s]
        left = []
        right = []
        for ind,l in enumerate(s):
            if l=="(":
                left.append(ind)
            elif l==")":
                try:
                    left.pop()
                except:
                    right.append(ind)
        for ind in left+right:
            s[ind] = "#"
        s = "".join(s)
        s = s.replace("#","")
        return s