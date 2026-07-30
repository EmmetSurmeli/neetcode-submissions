class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = height[0], height[-1]
        total = 0
        while l <= r:
            if lmax < rmax:
                if lmax > height[l]:
                    total += lmax - height[l]
                else:
                    lmax =  height[l]
                l += 1
            else:
                if rmax > height[r]:
                    total += rmax - height[r]
                else:
                    rmax = max(rmax, height[r])
                r -= 1
        return total