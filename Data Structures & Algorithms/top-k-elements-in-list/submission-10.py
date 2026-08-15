class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = [[] for _ in range(len(nums) + 1)]
        for i, j in count.items():
            arr[j].append(i)
        output = []
        for i in range(len(nums), -1, -1):
            for j in arr[i]:
                if k == 0:
                    return output
                output.append(j)
                k -= 1
        return output