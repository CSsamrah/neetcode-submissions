class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater=0
        width,height=0,0
        left,right=0,len(heights)-1
        while(left<right):
                width=right-left
                height=min(heights[left],heights[right])
                currWater=width*height
                maxWater=max(maxWater,currWater)
                if heights[left]<heights[right]:
                    left+=1
                else:
                    right-=1
        return maxWater


        