# Validate Parentheses
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
# The input string s is valid if and only if:
# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

# Example 1:
# Input: s = "[]"
# Output: true

# Example 2:
# Input: s = "([{}])"
# Output: true

# Example 3:
# Input: s = "[(])"
# Output: false
# Explanation: The brackets are not closed in the correct order.

# Constraints:
# 1 <= s.length <= 1000

class Solution:
    def isValid(self, s):
        stack = []
        hash_dict = { ')' : '(', ']' : '[', '}' : '{' }

        for i in s:
            
            if i in hash_dict:
                if len(stack) != 0 and stack[-1] == hash_dict[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        if len(stack) == 0:
            return True
        else:
            return False



res = Solution()
print(res.isValid("([{}])"))
        