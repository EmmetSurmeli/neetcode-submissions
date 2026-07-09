from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       # Brute force
       # counter: keep track of frequency of each number
       # Go through counter and find which element matches up with 
       # highest frequency: max (count.values()), then go through 
       # dictionary until it shows up, add that to output array, 
       # and then delete from the dictionary. Redo the max, 
       # then go through it again
        count = Counter(nums)
        output = list()
        while k > 0:
            curMax = max(count.values())
            for i in count.keys():
                if count[i] == curMax:
                    output.append(i)
                    count.pop(i)
                    k -= 1
                    break
        return output
            


