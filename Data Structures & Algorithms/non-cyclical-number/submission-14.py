class Solution:
    def isHappy(self, n: int) -> bool:
        mySet = set()
        summ = n
        while summ not in mySet:
            mySet.add(summ)
            n = summ
            summ = 0
            while n > 0:
                summ += (n % 10) * (n % 10)
                n = n // 10
            if summ == 1:
                return True
        return False