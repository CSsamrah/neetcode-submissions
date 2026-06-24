class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates={}
        for r in range(len(nums)):
            duplicates[nums[r]]=duplicates.get(nums[r],0)+1
            if duplicates[nums[r]]>1:
                return True
        return False 

        