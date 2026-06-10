class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diction = {}
        arr = []
        for num in nums:
            if num not in diction:
                diction[num] = 0
            diction[num] = diction[num] + 1
        for num, cnt in diction.items():
            arr.append([cnt, num])
        arr.sort()

        output = []
        while len(output) < k:
            output.append(arr.pop()[1])
        return output
