import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        p_queue = [-x for x in stones]
        heapq.heapify(p_queue)
        while len(p_queue) > 1:
            largest = -1 * heapq.heappop(p_queue)
            smaller = -1 * heapq.heappop(p_queue)
            if smaller < largest:
                heapq.heappush(p_queue, -(largest - smaller))
        if p_queue:
            return -1 * heapq.heappop(p_queue)
        else:
            return 0
