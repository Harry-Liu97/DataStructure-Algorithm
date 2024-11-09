# String Encode and Decode
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
# Please implement encode and decode

# Example 1:
# Input: ["neet","code","love","you"]
# Output:["neet","code","love","you"]

# Example 2:
# Input: ["we","say",":","yes"]
# Output: ["we","say",":","yes"]

# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.

class Solution:

    def encode(self, strs):
        if not strs:
            return ""
        
        sizes, res = [], ""
        for s in strs:
            sizes.append(len(s))

        for sz in sizes:
            res += str(sz)
            res += ','
        res += '#'

        for s in strs:
            res += s
        return res

    def decode(self, s):
        if not s:
            return []
        
        sizes, res, i = [], [], 0

        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
            
        i += 1

        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res
    
res = Solution()
print(res.encode(["neet","code","love","you"]))
print(res.decode(res.encode(["neet","code","love","you"])))