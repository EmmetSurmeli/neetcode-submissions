class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, lmax, rmax = 0, len(height) - 1, height[0], height[-1]
        trapped = 0
        while l <= r:
            if lmax < rmax:
                if lmax > height[l]:
                    trapped += lmax - height[l]
                else:
                    lmax = height[l]
                l += 1
            else:
                if rmax > height[r]:
                    trapped += rmax - height[r]
                else:
                    rmax = height[r]
                r -= 1
        return trapped
