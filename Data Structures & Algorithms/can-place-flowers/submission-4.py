class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = 0
        if len(flowerbed) == 1:
            return n == 0 if flowerbed[0] == 1 else n <= 1
        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                    flowers += 1
                    flowerbed[0] = 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                    flowers += 1
                    flowerbed[i] = 1
            else:
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                    flowers += 1
                    flowerbed[i] = 1
        return n <= flowers