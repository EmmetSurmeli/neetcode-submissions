class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j) - ord("a")] += 1
            tupe = tuple(count)
            if tupe in myDict:
                myDict[tupe].append(i)
            else:
                myDict[tupe] = [i]
        output = []
        for i in myDict.values():
            output.append(list(i))
        return output