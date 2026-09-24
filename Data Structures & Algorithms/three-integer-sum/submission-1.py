class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=set()
        for i in range(len(nums)):
            seen=set()
            for j in range(i+1,len(nums)):
                    required=-(nums[i]+nums[j])
                    if required in seen :
                        triplets=tuple(sorted([nums[i],nums[j],required]))
                        result.add(triplets)
                    seen.add(nums[j])
        
        return [list(triplet)for triplet in result]



            



            
        