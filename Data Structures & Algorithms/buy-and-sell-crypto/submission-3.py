class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minbuy = prices[0]
        for p in prices:
            maxP = max(maxP,p-minbuy)
            minbuy = min(minbuy,p)
        return maxP