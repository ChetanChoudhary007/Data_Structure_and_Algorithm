class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy=prices[0]
        profit=0
        profit_alt=0
        for i in range(1,len(prices)):
            profit=max(profit,prices[i]-buy)
            buy=min(buy,prices[i])

            # checking for the profit through alternatives
            summ=prices[i]-prices[i-1]
            if summ >= 0:
                profit_alt+=summ
                
        return max(profit,profit_alt)