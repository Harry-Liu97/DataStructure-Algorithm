# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

class Solution:
    def maxProfit(self, prices):

        # Dynamic Programming - dp array

        # Handle special cases
        if len(prices) == 1:
            return 0
        
        # dp array - store the minimum integer from the starting point prices[0] to the previous position of the current location
        # Treat the current element as the selling price
        dp = [0] * (len(prices) + 1)

        # Define the subproblem
        dp[0] = 0
        dp[1] = prices[0]
        result = 0

        # Traverse the array starting from index 2
        for day in range(2, len(prices) + 1):

            # State transition equation
            dp[day] = min(dp[day - 1], prices[day - 2])
            
            result = max(result, prices[day - 1] - dp[day])

        return result
        
res = Solution()
print(res.maxProfit([7,1,5,3,6,4]))