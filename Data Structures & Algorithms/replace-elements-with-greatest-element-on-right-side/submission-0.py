class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        highest = arr[-1]
        arr[-1] = -1
        for i in range (len(arr) -2, -1, -1):
            if highest > arr[i]:
                arr[i] = highest
            else:
                temp = arr[i]
                arr[i] = highest
                highest = temp
        return arr
                