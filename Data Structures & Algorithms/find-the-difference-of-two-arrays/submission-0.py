class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set2 = set(nums2)
        set1 = set(nums1)
        res = [] 
        for i in range(len(nums1)):
            if nums1[i] in set2:
                set2.remove(nums1[i])
                set1.remove(nums1[i])
        return [list(set1), list(set2)]