from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # keep track of frequency in list: bucket[1] is lsit of all
        # numbers who appear with frequency 1.
        # return top k 
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        out = []
        for i in count.keys():
            freq[count[i]].append(i)
        for i in range(len(freq) - 1, -1, -1):
            if k == len(out):
                return out
            for num in freq[i]:
                out.append(num)
                if k == len(out):
                    return out