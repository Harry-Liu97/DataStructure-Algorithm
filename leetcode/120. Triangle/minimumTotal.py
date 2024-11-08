# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

# Example 1:
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

# Example 2:
# Input: triangle = [[-10]]
# Output: -10

class Solution:
    def minimumTotal(self, triangle):

        # Dynamic Programming - dp array

        length_triangle = len(triangle)

        # Define a 2D dp array
        dp = [[0] * length_triangle for _ in range(length_triangle)]

        # Set the initial value
        dp[0] = triangle[0]

        # Column index boundary for the first row
        col_index_edge = 1

        # dp[row][column] stores the minimum path sum at position (row, column) in the original array
        for row in range(1, len(triangle)):
            # Column index boundary for each row in the triangle
            col_index_edge += 1

            for column in range(0, col_index_edge):
                # Left boundary check
                if column == 0:
                    dp[row][column] = dp[row - 1][column] + triangle[row][column]

                # Right boundary check
                elif column == col_index_edge - 1:
                    dp[row][column] = dp[row - 1][column - 1] + triangle[row][column]

                # Middle part check
                else:
                    # State transition equation
                    dp[row][column] = min(dp[row - 1][column], dp[row - 1][column - 1]) + triangle[row][column]
                    
        # Return the minimum path sum
        return min(dp[-1])

res = Solution()
print(res.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
    