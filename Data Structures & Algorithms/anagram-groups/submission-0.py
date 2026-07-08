class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        for i in strs:
            arr = [0] * 26
            for j in i:
                arr[ord(j) - ord('a')] += 1
            tupe = tuple(arr)
            if tupe in myDict:
                myDict[tupe].append(i)
            else:
                myDict[tupe] = [i]
        return list(myDict.values())
