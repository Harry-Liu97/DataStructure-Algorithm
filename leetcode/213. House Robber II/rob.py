# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 3:
# Input: nums = [1,2,3]
# Output: 3

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000

class Solution:
    def rob(self, nums):
        '''
        Dynamic Programming - DP Array (Subproblem Array)
        Transform the circular arrangement of rooms into two linear arrangements.
        Note: There are two core approaches to simplifying complex problems in algorithmic questions: 
        "Divide and Conquer" and "Reduce and Conquer." 
        This problem uses "Divide and Conquer" by breaking the circular problem into two smaller linear subproblems.
        '''

        if len(nums) <= 1:
            return nums[-1]

        # Case 1: Do not rob the last house, reducing the total number of houses by one
        dp_last = [0] * len(nums)
        dp_last[0] = 0
        dp_last[1] = nums[0]

        # Case 2: Do not rob the first house, reducing the total number of houses by one
        dp_first = [0] * len(nums)
        dp_first[0] = 0
        # If the first house is not robbed, the maximum amount after robbing one house is the value of the second house
        dp_first[1] = nums[1]

        # Analyze subproblems
        for room in range(2, len(nums)):
            # State transition equations for both cases
            dp_last[room] = max(dp_last[room - 1], dp_last[room - 2] + nums[room - 1])
            dp_first[room] = max(dp_first[room - 1], dp_first[room - 2] + nums[room])

        # Return the maximum amount from the two cases
        return max(dp_first[len(nums) - 1], dp_last[len(nums) - 1])
    
res = Solution()
print(res.rob([1,2,3,1]))