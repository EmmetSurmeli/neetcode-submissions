class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Time: O(n + m)
        #space: O(n)
        myList = []
        set1 = set(nums1)
        for i in nums2:
            if i in set1:
                myList.append(i)
                set1.remove(i)
        return myList