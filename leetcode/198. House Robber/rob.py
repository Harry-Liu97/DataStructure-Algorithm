# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

class Solution:
    def rob(self, nums):
        '''
            Dynamic Programming — Iterative
            Bottom-up approach (using DP array)
        '''
        # If nums does not contain any elements, return 0 (no houses to rob)
        if not nums:
            return 0

        n = len(nums)
        # The length of the dp array is n + 1, +1 is to include the last house and avoid omissions
        dp = [0] * (n + 1)
        # Define the subproblem: the maximum amount when robbing 0 houses is 0
        dp[0] = 0
        # Define the subproblem: the maximum amount when robbing 1 house
        dp[1] = nums[0]
        # Start iterating dp indices from 2, k represents the number of houses robbed, iterate until k = n, i.e., n + 1
        for k in range(2, n + 1):
            # Two scenarios of robbing, choose the maximum one
            dp[k] = max(dp[k - 1], nums[k - 1] + dp[k - 2])
        
        return dp[-1]
    
res = Solution()
print(res.rob([2,7,9,3,1]))