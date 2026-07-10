class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 1, len(height) - 2
        lmax, rmax = height[0], height[-1]
        total = 0
        while l <= r:
            if lmax < rmax:
                if lmax < height[l]:
                    lmax = height[l]
                else:
                    total += lmax - height[l]
                l += 1
            else:
                if rmax < height[r]:
                    rmax = height[r]
                else:
                    total += rmax - height[r]
                r -= 1
        return total