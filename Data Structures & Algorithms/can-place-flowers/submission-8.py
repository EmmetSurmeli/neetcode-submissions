class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter = 0 if flowerbed[0] else 1
        for i in flowerbed:
            if i:
                n -= int((counter - 1) / 2)
                counter = 0
            else:
                counter += 1
        n -= counter // 2
        return n <= 0