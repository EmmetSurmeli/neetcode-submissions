class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mySet = set()
        set1 = set(nums1)
        for i in nums2:
            if i in set1:
                mySet.add(i)
        return list(mySet)