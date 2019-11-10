class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        res = [[0 for i in range(len(colsum))] for i in range(2)]
        one = 0
        for ind,i in enumerate(colsum):
            if i==2:
                upper -= 1
                lower -= 1
                if upper<0 or lower<0:
                    return []
                res[0][ind] = 1
                res[1][ind] = 1
            elif i == 1:
                one += 1
        if upper + lower != one:
            return []
        else:
            for ind,i in enumerate(colsum):
                if i==1:
                    if upper>0:
                        res[0][ind] = 1
                        upper -= 1
                    else:
                        res[1][ind] = 1
                        lower -= 1
            return res
            
        
                