class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix,suffix = 1,1
        n = len(nums)
        ans = [1]*n

        for i in range(n):
            ans[i]=prefix
            prefix*= nums[i]
        
        for j in reversed(range(n)):
            ans[j]*=suffix
            suffix*=nums[j]
        return ans