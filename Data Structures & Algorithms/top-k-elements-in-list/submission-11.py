class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ranking = [[] for _ in range(len(nums) + 1)]
        myDict = {}
        for i in nums:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1
        for i, j in myDict.items():
            ranking[j].append(i)
        output = []
        for i in range(len(ranking) - 1, 0, -1):
            for j in ranking[i]:
                if k <= 0:
                    return output
                output.append(j)
                k -= 1
        return output