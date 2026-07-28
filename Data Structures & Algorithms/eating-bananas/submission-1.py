class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        while left <= right:
            mid = left + (right - left) // 2
            time = self.timeTaken(piles, mid)
            if time > h:
                left = mid + 1
            else:
                right = mid - 1
        return left


    def timeTaken(self, bananas: List[int], rate: int):
        total = 0
        for i in bananas:
            total -= -i // rate
        return total
        