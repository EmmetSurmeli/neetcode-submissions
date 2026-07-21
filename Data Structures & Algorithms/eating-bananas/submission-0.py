class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Upper bound: max(piles), as h is always >= piles.length

        upper = max(piles) #O(n)
        lower = 1
        while lower <= upper:
            mid = lower + (upper - lower) // 2
            time = self.timeTaken(piles, mid)
            if time > h:
                lower = mid + 1
            else:
               upper = mid - 1
        return lower
    # rate != 0, lower can never be < 1
    def timeTaken(self, piles: List[int], rate: int) -> int:
        total = 0
        for i in piles:
            total -= -i // rate
        return total