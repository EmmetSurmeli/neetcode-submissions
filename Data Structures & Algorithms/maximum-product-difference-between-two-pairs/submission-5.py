class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        arr = [float('inf')] * 2 + [float('-inf')] * 2
        for i in nums:
            if i <= arr[0]:
                arr[1] = arr[0]
                arr[0] = i
            elif i < arr[1]:
                arr[1] = i
            if i >= arr[3]:
                arr[2] = arr[3]
                arr[3] = i
            elif i > arr[2]:
                arr[2] = i
        return arr[3] * arr[2] - arr[1] * arr[0]