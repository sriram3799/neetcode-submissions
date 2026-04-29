class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        res = []
        bucket = [[] for _ in range(len(nums)+1)]

        for i,c in freq.items():
            bucket[c].append(i)
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res