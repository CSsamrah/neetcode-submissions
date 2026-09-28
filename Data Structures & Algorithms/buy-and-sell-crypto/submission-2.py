class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        l=0
        r=1
        while(r<len(prices)):
            buy=prices[l]
            if prices[l]<prices[r]:
                sell=prices[r]
                profit=sell-buy
                maxProfit=max(maxProfit,profit)
            else:
                l=r
            r+=1
        return maxProfit


        