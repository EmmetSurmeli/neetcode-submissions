class Solution:
    def largestGoodInteger(self, num: str) -> str:
        currNum = int(num[0])
        currMax = 0 
        for i in range(1, len(num) - 1):
            if int(num[i]) >= int(currMax):
                if num[i] == num[i - 1] and num[i] == num[i + 1]:
                    currMax = num[i]
        return '' if currMax == 0 else currMax * 3