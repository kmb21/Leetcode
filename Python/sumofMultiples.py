def sumOfMultiples(self, n: int) -> int:
        sum357 = 0
        for i in range(1,n+1):
            if i%3 == 0:
                sum357 += i
            elif i%7 == 0:
                sum357 += i
            elif i%5 == 0:
                sum357+=i
        return sum357
    