class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        diction = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in diction:
                diction[key] = []
            diction[key].append(word)
        return list(diction.values())