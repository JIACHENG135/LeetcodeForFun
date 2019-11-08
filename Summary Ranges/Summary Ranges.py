class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        i = 0
        counter = 0
        res = []
        nums.append(float('inf'))
        while i<len(nums)-1:
            #print(i)
            if nums[i+1]!= nums[i]+1:
                if nums[i+1] != nums[i]:
#                    print(i)
                    k = i
                    while nums[k-1]== nums[k]-1 or nums[k-1] == nums[k]:
                        k = k-1
                    if k!=i:
                        res.append(str(nums[k])+'->'+str(nums[i]))
                    else:
                        res.append(str(nums[i]))
                    
            else:
                counter += 1
            i += 1
        return res