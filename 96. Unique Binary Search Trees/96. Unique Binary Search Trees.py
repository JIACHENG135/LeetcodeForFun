class Solution:
    def __init__(self):
        self.mem = dict()
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.mem:
            return self.mem[n]
        if n == 0 or n == 1:
            self.mem[n] = 1
            return self.mem[n]
        elif n==2:
            self.mem[n]= 2
            return self.mem[n]
        else:
            sum_all = 0
            for i in range(n):
                sum_all += self.numTrees(i)*self.numTrees(n-i-1)
            self.mem[n] = sum_all
            return sum_all