class Solution:
    def maxArea(self, height: list[int]) -> int:
        n=len(height)
        l,r,mArea=0,n-1,0
        while l<=r:
            area=min(height[r],height[l])*(r-l)
            mArea=max(mArea,area)
            if(height[r]>height[l]):l+=1
            else: r-=1
        return mArea