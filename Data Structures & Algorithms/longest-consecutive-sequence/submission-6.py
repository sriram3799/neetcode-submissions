class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for num in numset:
            if num-1 not in numset:
                l = 1
                c = num
                while c+1 in numset:
                    c+=1
                    l+=1
                longest = max(longest,l)
        return longest