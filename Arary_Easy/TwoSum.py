class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d={}
        for index,value in enumerate(nums):
            res= target - value
            if res in d:
                return [d[res],index]
            d[value]=index 