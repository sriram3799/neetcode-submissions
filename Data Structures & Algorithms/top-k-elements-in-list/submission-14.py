class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        bucket = [[] for _ in range(len(nums)+1)]
        freq = collections.Counter(nums)
        for i,count in freq.items():
            bucket[count].append(i)
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res