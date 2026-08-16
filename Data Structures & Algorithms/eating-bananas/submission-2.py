class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        best = max(piles)
        while low <= high:
            mid = low + (high - low) // 2
            time = self.time(piles, mid)
            if time > h:
                low = mid + 1
            else:
                best = min(best, mid)
                high = mid - 1
        return best
    def time(self, arr: List[int], rate: int):
        total = 0
        for i in arr:
            total += -(-i // rate)
        return total