class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)[::-1]
        if not s[-1].isdigit():
            t = s[-1]
            m = t + s[:len(s)-1]
        else:
            m = s

        x = int(m)
        if x < -2**31 or x > 2**31 -1:
            return 0
        return x