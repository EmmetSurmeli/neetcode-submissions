class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        diction = {}
        tempList = []

        for word in range(0,len(strs)): #sorting each word
            tempList.append("".join(sorted(strs[word])))

        #getting all the different anagram letters
        mySet = set()
        for n in tempList:
            mySet.add(n)
        
        #creating dictionary with the keys of the different letters, empty values
        keys = []
        for x in mySet:
            keys.append(x)
        diction = {key: [] for key in keys} 

        #adding each word in strs to appropriate list in dict
        for x in mySet:
            for i in range(0, len(tempList)):
                if x == tempList[i]:
                    diction[x].append(strs[i])

        #creating and outputting final list
        finalList = []
        for j in diction:
            finalList.append(diction[j])
        return finalList