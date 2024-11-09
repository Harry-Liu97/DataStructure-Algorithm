# Is Palindrome
# Given a string s, return true if it is a palindrome, otherwise return false.
# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Example 1:
# Input: s = "Was it a car or a cat I saw?"
# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

# Example 2:
# Input: s = "tab a cat"
# Output: false
# Explanation: "tabacat" is not a palindrome.

# Constraints:

# 1 <= s.length <= 1000
# s is made up of only printable ASCII characters.

class Solution:
    def isPalindrome(self, s):

        s_new = ''.join(c.lower() for c in s if c.isalnum())
        left = 0
        right = len(s_new) - 1
        
        while left < right:
            if s_new[left] != s_new[right]:
                return False
            
            left += 1
            right -= 1
            
        return True
    
res = Solution()
print(res.isPalindrome("Was it a car or a cat I saw?"))