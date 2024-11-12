# Longest Substring Without Duplicates
# Given a string s, find the length of the longest substring without duplicate characters.
# A substring is a contiguous sequence of characters within a string.

# Example 1:
# Input: s = "zxyzxyz"
# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.

# Example 2:
# Input: s = "xxxx"
# Output: 1

# Constraints:

# 0 <= s.length <= 1000
# s may consist of printable ASCII characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        chrStore = [s[0]]
        l, res = 0, len(chrStore)

        for r in range(1, len(s)):

            while s[r] in chrStore:
                chrStore.remove(s[l])
                l += 1
            chrStore.append(s[r])
            res = max(res, len(chrStore))

        return res

res = Solution()
print(res.lengthOfLongestSubstring(s="zxyzxyz"))