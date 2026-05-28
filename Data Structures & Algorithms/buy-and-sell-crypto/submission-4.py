class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minbuy = prices[0]
        for p in prices:
            sell = p-minbuy
            maxP = max(maxP,sell)
            minbuy = min(minbuy,p)
        return maxP