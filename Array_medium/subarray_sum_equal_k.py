class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        
        # initialize the length of the array 
        n=len(nums)

        # make an empty dictionary that stores the sums and its occurence
        record={0:1}
        
        # Main Logic

        # initialize the sum and count of subarrays
        summ=0
        count=0
        
        # main logic 
        for i in nums:
            # adding the value in sum
            summ+=i
            
            # calculate prefix sum
            prefix_sum=summ-k

            # checking for prefix in the dictionary
            if prefix_sum in record:
                count+=record[prefix_sum]
            
            # adding the count of sums in the dictionary
            if summ in record:
                record[summ]+=1
            else:
                record[summ]=1
            
        #return the count 
        return count