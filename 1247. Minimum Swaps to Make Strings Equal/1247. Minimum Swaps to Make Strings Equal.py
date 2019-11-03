class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        wait = 0
        ct = collections.Counter()
        xy = collections.Counter()
        for i in range(len(s1)):
            if s1[i]!=s2[i]:

                xy[s1[i]] += 1

        # print(xy)
        if xy["x"]%2!=0:
            if xy["y"]%2==0:
                return -1
            else:
                return xy["x"]//2 + xy["y"]//2 + 2
        else:
            if xy["y"]%2 !=0:
                return -1
            else:
                return xy["x"]//2 + xy["y"]//2
                