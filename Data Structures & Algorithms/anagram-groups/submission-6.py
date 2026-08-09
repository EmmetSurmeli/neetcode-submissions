class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        for word in strs:
            arr = [0] * 26
            for letter in word:
                arr[ord(letter) - ord('a')] += 1
            if tuple(arr) in myDict:
                myDict[tuple(arr)].append(word)
            else:
                myDict[tuple(arr)] = [word]
        output = []
        for i in myDict.values():
            output.append(i)
        return output