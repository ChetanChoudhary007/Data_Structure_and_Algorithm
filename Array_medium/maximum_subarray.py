class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
    
        #Optimal Solution:
        summ=0
        maxi= float('-inf')
        for i in nums:
            summ=summ+i
            if summ>maxi:
                maxi=summ
            if summ<0:
                summ=0
        return maxi