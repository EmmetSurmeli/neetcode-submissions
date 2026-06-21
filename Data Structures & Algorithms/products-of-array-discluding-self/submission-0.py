class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # BRUTE FORCE
        i = 0
        output = []
        while i < len(nums):
            j = 0
            product = 1
            while j < len(nums):
                if i != j:
                    product = product * nums[j]
                j += 1
            i += 1
            output.append(product)
        return output