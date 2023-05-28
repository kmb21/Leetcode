class Solution:
    def reverseBits(self, n: int) -> int:
        x = bin(n)[2:][::-1] 
        x += "0"*(32-len(x))
        return int(x,2)