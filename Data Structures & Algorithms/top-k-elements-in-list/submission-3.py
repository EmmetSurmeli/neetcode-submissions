class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for _ in range(len(nums) + 1)]
        myDict = Counter(nums)
        for i in myDict:
            arr[myDict[i]].append(i)
        output = []
        for i in range(len(arr) - 1, -1, -1):
            if k == 0:
                return output
            for j in arr[i]:
                output.append(j)
                k -= 1
            
        