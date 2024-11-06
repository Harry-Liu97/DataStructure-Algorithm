# Is Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true

# Example 2:
# Input: s = "jar", t = "jam"
# Output: false

# Constraints:
# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s, t):
        hash_s = {}
        hash_t = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] in hash_s:
                hash_s[s[i]] += 1
            else:
                hash_s[s[i]] = 1

            if t[i] in hash_t:
                hash_t[t[i]] += 1
            else:
                hash_t[t[i]] = 1
        
        return hash_s == hash_t

res = Solution()
print(res.isAnagram(s = "racecar", t = "carrace"))
        