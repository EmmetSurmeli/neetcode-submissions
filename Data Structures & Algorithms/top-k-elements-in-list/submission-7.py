class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = [[] for _ in range(len(nums))]
        for i, j in count.items():
            arr[j - 1].append(i)
        output = []
        for i in range(len(nums) - 1, -1, -1):
            if k == 0:
                return output
            for j in arr[i]:
                output.append(j)
                k -= 1
        return output