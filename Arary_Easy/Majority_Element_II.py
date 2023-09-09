import math
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        final_list=[]
        records={}
        n=len(nums)
        limit=math.floor(n/3)
        if n < 2:
            return nums
        for i in nums:
            if i in records:
                records[i]+=1
            else:
                records[i]=1
        
        for i in records:
            if records[i] > limit:
                final_list.append(i)
    
        return final_list