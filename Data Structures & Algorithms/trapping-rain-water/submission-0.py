class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        current = 0
        res = 0
        max_l, max_r = height[l], height[r]
        while l < r:
            if (max_l < max_r):
                current = l + 1
                if(max_l - height[current] > 0):
                    res += max_l - height[current]
                if(height[current] > max_l):
                    max_l = height[current]
                l += 1
            else:
                current = r - 1
                if(max_r - height[current] > 0):
                    res += max_r - height[current]
                if(height[current] > max_r):
                    max_r = height[current]
                r -= 1
        return res
                
                
