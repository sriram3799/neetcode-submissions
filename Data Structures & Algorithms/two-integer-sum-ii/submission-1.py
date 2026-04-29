class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1
        cs = 0
        while l<r:
            cs = numbers[l]+numbers[r]
            if l<r and cs>target:
                r-=1
            elif l<r and cs<target:
                l+=1
            else:
                return [l+1,r+1]
                l+=1
                r-=1
        return []