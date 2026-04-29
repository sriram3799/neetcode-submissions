class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i,v in enumerate(nums):
            d = target-v
            if v in hm:
                return [hm[v],i]
            hm[d] = i
        return []