class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxim = 0
        tempstr = ""
        i = 0
        while i < len(s):
            if s[i] in tempstr:
                n = len(tempstr)
                maxim = max(maxim, n)
                i -= n-1
                tempstr = ""
            else:
                tempstr += s[i]
                i+=1
        return max(len(tempstr), maxim)

