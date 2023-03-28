class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        longest = 0
        substr = ""
        for i in range(len(s)):
            m = len(s)
            palin = s[i:m]
            while palin[::1] != palin[::-1]:
                m -= 1
                palin = s[i:m]
            if (len(palin)) > longest:
                longest = len(palin)
                substr = palin  
              
        return substr
        