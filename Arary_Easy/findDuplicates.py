class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        visited=[0]*len(nums)
        for i in nums:
            if visited[i]==0:
                visited[i]+=1
            else:
                return i
        