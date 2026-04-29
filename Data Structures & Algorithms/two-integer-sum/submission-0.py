class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i,val in enumerate(nums):
            diff = target-val
            if val in hm:
                return [hm[val], i]
            hm[diff]=i
        return []