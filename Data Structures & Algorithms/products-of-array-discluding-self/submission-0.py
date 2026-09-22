class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

#for time complexity of o(n) and space o(1)
        ans=[1]*len(nums)

        #for prefix save it into ans array
        for i in range(1,len(nums),1):
            ans[i]=ans[i-1]*nums[i-1]
        
        #for suffix we need to save it in suffix variable and multiply it with ans[i] array
        suffix=1
        for i in range(len(nums)-2,-1,-1):
            suffix=suffix*nums[i+1]
            ans[i]=ans[i]*suffix
        return ans 


        #space complexity is o(n) here 
        # finalProduct=[]
        # for i in range(len(nums)):
        #     product=1
        #     for j in range(len(nums)):
        #         if i!=j:
        #             product*=nums[j]
        #     finalProduct.append(product)
        # return finalProduct
               