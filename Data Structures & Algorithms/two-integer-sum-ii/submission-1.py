class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer: Start at beginning, do binary search
        #if cant find with right pointer, then move to the right with
        #left pointer and repeat
        for i in range(len(numbers)):
            l = i
            r = len(numbers) - 1
            
            while l <= r:
                mid = (l + r) // 2
                if numbers[i] + numbers[mid] == target:
                    return [i + 1, mid + 1]
                if numbers[mid] > target - numbers[i]:
                    r = mid - 1
                else:
                    l = mid + 1
