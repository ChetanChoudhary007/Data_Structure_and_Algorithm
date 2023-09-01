class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        # define the size
        n=len(nums)

        #finding the break point 
        index=-1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]: 
                index=i 
                break  
        
        # if the next permutation is not available, return reversed nums
        if index==-1:
            nums[::]=nums[::-1]
            return

        #finding the smallest greater number in right list of the index, and swap it
        for j in range(n-1,index,-1):
            if nums[j] > nums[index]:
                nums[j],nums[index]=nums[index],nums[j]
                break

        #revesrse the right list of the index 
        nums[::]=nums[:index+1]+nums[index+1:][::-1]