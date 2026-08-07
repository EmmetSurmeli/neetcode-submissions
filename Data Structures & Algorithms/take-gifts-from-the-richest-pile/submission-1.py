import math
import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-gift for gift in gifts]
        heapq.heapify(heap)
        for _ in range(k):
            largest = -heapq.heappop(heap)
            sqrt = math.isqrt(largest)
            heapq.heappush(heap, -sqrt)
        return -sum(heap)