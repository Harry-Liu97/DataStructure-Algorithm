# Max Water Container
# You are given an integer array heights where heights[i] represents the height of the ith bar
# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

# Example 1:
# Input: height = [1,7,2,5,4,7,3,6]
# Output: 36

# Example 2:
# Input: height = [2,2,2]
# Output: 4

# Constraints:

# 2 <= height.length <= 1000
# 0 <= height[i] <= 1000

class Solution:
    def maxArea(self, heights):
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)

            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        return res
    
res = Solution()
print(res.maxArea([1,7,2,5,4,7,3,6]))