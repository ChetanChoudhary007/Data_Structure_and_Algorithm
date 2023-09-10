class Solution:
    
    def maxProfit(self, prices: list[int]) -> int:
        # intialize the buy variable and profit
        buy=prices[0]
        profit=0

        # iterates throught the list
        for price in prices[1:]:
            profit=max(profit,price-buy)
            buy=min(price,buy)
        
        # return the maximum profit
        return profit