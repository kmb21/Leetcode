class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindromes = {}
        maxlength = 0
        t = s
        while len(t) > maxlength:
            n = 1
            palindrome = t
            while len(palindrome) > maxlength:
                if palindrome == palindrome[::-1]:
                    maxlength = max(len(palindrome), maxlength)
                    palindromes[maxlength] = palindrome[:len(palindrome)]
                    break
                palindrome = t[:len(t)-n]
                n+=1
            t = t[1:]
            
        return palindromes[maxlength]