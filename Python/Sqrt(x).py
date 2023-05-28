class Solution:
    def mySqrt(self, x: int) -> int:
        #Using newton Raphson's method
        if x < 2:
            return x

        temp = x
        while True:
            root = 0.5*(temp+x/temp)
            if abs(root-temp) < 1e-7:
                return int(root)
            temp = root