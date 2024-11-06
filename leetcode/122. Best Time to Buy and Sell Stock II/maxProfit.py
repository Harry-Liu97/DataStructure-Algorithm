# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.

# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.

# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

class Solution:
    def maxProfit(self, prices):

        # Dynamic Programming - dp array

        # dp[day][0]: Maximum profit on day `day` after completing a transaction and not holding any stock
        # dp[day][1]: Maximum profit on day `day` after completing a transaction and holding one stock
        dp = [[0, 0] for _ in range(len(prices))]

        # Maximum profit on day 0
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        # Starting from day 1
        for day in range(1, len(prices)):
            
            # State transition for dp[day][0]: If no stock is held after transactions on this day, possible states:
            # 1: No stock was held the previous day.
            # 2: A stock was held the previous day, and it is sold today for profit.
            dp[day][0] = max(dp[day - 1][0], dp[day - 1][1] + prices[day])

            # State transition for dp[day][1]: Using similar logic, possible states:
            # 1: A stock was already held the previous day.
            # 2: No stock was held the previous day, and a stock is bought today, reducing profit.
            dp[day][1] = max(dp[day - 1][1], dp[day - 1][0] - prices[day])

        # On the last day, the profit of holding stock will definitely be lower than not holding stock.
        return dp[len(prices) - 1][0]