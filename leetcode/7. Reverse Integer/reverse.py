# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

# Constraints:
# -2^31 <= x <= 2^31 - 1

class Solution:
    def reverse(self, x):
        if x >= 0:
            new_x = str(x)[::-1]
            if  -2 ** 31 <= int(new_x) <= 2**31 - 1:
                return int(new_x)
            else:
                return 0
        else:
            new_x = '-' + str(x)[:0:-1]
            if -2 ** 31 <= int(new_x) <= 2 ** 31 - 1:
                return int(new_x)
            else:
                return 0

res  = Solution()
print(res.reverse(123))