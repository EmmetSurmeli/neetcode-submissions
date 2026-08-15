class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = height[0], height[-1]
        area = 0
        while l < r:
            if lmax < rmax:
                l += 1
                area += max(0, lmax - height[l])
                lmax = max(lmax, height[l])
            else:
                r -= 1
                area += max(0, rmax - height[r])
                rmax = max(rmax, height[r])
        return area