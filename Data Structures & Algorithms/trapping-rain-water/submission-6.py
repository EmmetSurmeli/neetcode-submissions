class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0] * len(height)
        for i in range(1, len(height)):
            if height[i - 1] > maxL[i - 1]:
                maxL[i] = height[i - 1]
            else:
                maxL[i] = maxL[i - 1]
        maxR = [0] * len(height)
        for i in range(len(height) - 2, -1, -1):
            if height[i + 1] > maxR[i + 1]:
                maxR[i] = height[i + 1]
            else:
                maxR[i] = maxR[i + 1]
        arr = [0] * len(height)
        for i in range(len(height)):
            arr[i] = min(maxL[i], maxR[i])
        total = 0
        for i in range(len(height)):
            total += max(0, arr[i] - height[i])
        return total