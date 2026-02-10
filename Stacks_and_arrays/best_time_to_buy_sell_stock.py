'''You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that 
stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.'''

# Solution: I need to know the minimum price and the maximum profit. I can save the minimum and update it as I iterate.
# If the current price - minimum price is grater than the maximum profit, I update the maximum profit. O(n) of time and O(1) of space.
# I don't care about the previous prices, I just need to know the minimum price and the maximum profit at each step. Each step is
# "the next day", so I can only compare the current price with the minimum price and the maximum profit.
from typing import List

class Solution: 
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
            
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4])) # 5
    print(solution.maxProfit([7,6,4,3,1])) # 0
