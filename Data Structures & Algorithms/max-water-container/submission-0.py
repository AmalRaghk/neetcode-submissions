class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        
        while l < r:
            width = r - l
            current_height = min(height[l], height[r])
            current_area = width * current_height
            
            max_area = max(max_area, current_area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_area