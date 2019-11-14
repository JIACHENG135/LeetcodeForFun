# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = -1
        
        a = 0
        for b in range(1,n):
            if knows(a,b):
                a = b
        for i in range(n):
            if knows(a,i) and a!=i:
                return -1
            if not knows(i,a) and a!=i:
                return -1
        return a