class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {} # {array ord letters : word}
        for i in strs:
            arr = [0] * 26
            for j in range(len(i)):
                arr[ord(i[j]) - ord('a')] += 1
            if tuple(arr) in myDict:
                myDict[tuple(arr)].append(i)
            else:
                myDict[tuple(arr)] = [i]
        return list(myDict.values())