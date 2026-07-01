from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        #BRUTE FORCE
        total = 0
        temp = Counter(chars)
        for i in words:
            for j in range(len(i)):
                if i[j] in temp and temp[i[j]] > 0:
                    temp[i[j]] -=1
                else:
                    break
                if j == len(i) - 1:
                    total += len(i)
            temp = Counter(chars)

        return total