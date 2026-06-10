class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diction = {}
        output = []
        for num in nums:
            if num not in diction:
                diction[num] = 0
            diction[num] = diction[num] + 1
        for i in range (0, k):
            highest = max(list(diction.values())) # the # of max occurrences
            key = next((j for j, v in diction.items() if v == highest), None)
            output.append(key)
            diction.pop(key)
            i += 1
        return output