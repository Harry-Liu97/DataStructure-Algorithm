# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

class Solution:
    def maxSubArray(self, nums):
    # Dynamic Programming - Iterative Approach
    # Idea:
    # If the previous element is greater than 0, add it to the current element.

        # Iterate through the indices of the nums array, starting from index 1
        for index in range(1, len(nums)):
            # If the previous element is greater than 0, add it to the current element, forming a new nums
            if nums[index - 1] > 0:
                nums[index] = nums[index] + nums[index - 1]

        # Return the maximum element in the array, representing the maximum sum of a subarray
        return max(nums)
    

res = Solution()
print(res.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))