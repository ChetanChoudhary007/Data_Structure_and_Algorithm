class Solution:
    def rotate(self, num: list[int],k:int) -> list[int]:
        #in case k is > then the size of array,
        # or in case k=size of the array,then there no need to rotate 
        n=len(num)
        k = k% n 
        num[:] = num[::-1]
        num[:k]=num[:k][::-1]
        num[k:n] = num[k:n][::-1]
        return num