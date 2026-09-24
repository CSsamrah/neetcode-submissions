import sys
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        longest=1
        count=0
        lastSmaller=-sys.maxsize - 1
        for i in range(0,len(nums)):
            if lastSmaller==nums[i]-1:
                count+=1
                lastSmaller=nums[i]
            elif lastSmaller!=nums[i]:
                count=1
                lastSmaller=nums[i]
            i=i+1
            longest=max(longest,count)
        return longest
            

        