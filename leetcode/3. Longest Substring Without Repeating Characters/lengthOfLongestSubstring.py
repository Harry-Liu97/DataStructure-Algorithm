# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
            Official approach - Sliding window (queue)
            A hash set is a data structure, and the code below uses a hash set to store non-repeating substrings
        '''
        # Hash set, used to record each non-repeating character
        hash_set = set()
        # Initial value of the right pointer, not moved initially, optimized to 0
        right = -1
        index_edge = len(s) - 1
        max_substring = 0
        for left in range(len(s)):
            if left != 0:
                # Sliding window (queue), every time the left pointer moves, the character at the last position is removed
                hash_set.remove(s[left - 1])
                # If the following conditions are met, the right pointer keeps moving to the right
            while right + 1 <= index_edge and s[right + 1] not in hash_set:
                hash_set.add(s[right + 1])
                right += 1
            if len(hash_set) > max_substring:
                max_substring = len(hash_set)
        return max_substring

    
res = Solution()
print(res.lengthOfLongestSubstring("abcabcbb"))
        