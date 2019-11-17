class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        for x in range(1, 7):
            ca = cb = 0
            for i in range(len(A)):
                if A[i] != x and B[i] != x:
                    break
            else:
                for i in range(len(A)):
                    if A[i] != x:
                        ca += 1
                    if B[i] != x:
                        cb += 1
                return min(ca, cb)
        return -1