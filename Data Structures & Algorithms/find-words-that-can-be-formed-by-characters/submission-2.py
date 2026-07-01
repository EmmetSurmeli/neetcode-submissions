class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
        count = [0] * 26
        for i in chars:
            count[ord(i) - ord('a')] += 1
        temp = count[:]
        for word in words:
            for j in range(len(word)):
                if temp[ord(word[j]) - ord('a')] > 0:
                    temp[ord(word[j]) - ord('a')] -=1
                else:
                    break
                if j == len(word) - 1:
                    total += len(word)
            for k in range(26):
                temp[k] = count[k]
        return total