# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Example 1:
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

# Example 2:
# Input: prices = [1]
# Output: 0

# Constraints:
# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000

class Solution:
    def maxProfit(self, prices):
        '''
            Dynamic Programming - dp array
            Approach and Solution - Official Explanation
        '''

        # dp[day][0]: Maximum profit when currently holding one stock
        # dp[day][1]: Maximum profit when not holding any stock and in the cooling-off period
        # dp[day][2]: Maximum profit when not holding any stock and not in the cooling-off period
        dp = [[0, 0, 0] for _ in range(len(prices))]

        # Define initial boundary values
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = 0
        
        for day in range(1, len(prices)):
            # State transition equations: possible scenarios
            # 1: Currently holding the stock that was already held on day - 1
            # 2: Buying on day, meaning no stock was held and no cooling-off period on day - 1
            dp[day][0] = max(dp[day - 1][0], dp[day - 1][2] - prices[day])

            # State transition equations
            # Entering the cooling-off period on day due to selling the stock, 
            # which means we must have held one stock on day - 1
            dp[day][1] = dp[day - 1][0] + prices[day]

            # State transition equations: possible scenarios
            # 1: No operation on day, and the cooling-off period was on day - 1
            # 2: No operation on day, and no cooling-off period was on day - 1
            dp[day][2] = max(dp[day - 1][1], dp[day - 1][2])

        # Return the maximum value among the three scenarios on the last day
        return max(dp[len(prices) - 1][0], dp[len(prices) - 1][1], dp[len(prices) - 1][2])
            
res = Solution()
print(res.maxProfit([1,2,3,0,2]))