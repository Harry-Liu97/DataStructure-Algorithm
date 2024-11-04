# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        ptr = 0

        # put all 0 in front of the array
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                # move pointer
                ptr += 1

        # put all 1 between all 0 and others(2)
        for j in range(len(nums)):
            if nums[j] == 1:
                nums[j], nums[ptr] = nums[ptr], nums[j]
                ptr += 1
        
        return nums


res = Solution()
print(res.sortColors([2,0,2,1,1,0]))
