class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stored = {}
        for x in s:
            if x in stored:
                stored[x] = stored[x] + 1
            else:
                stored[x] = 1
        for y in t:
            if y in stored: 
                stored[y] = stored[y] - 1
                if stored[y] == 0:
                    del stored[y]
            else:
                return False
        if not stored:
            return True
        else:
            return False