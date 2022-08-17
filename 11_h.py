class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, max_area = 0, 0
        j = len(height) - 1
        
        while j > i:
            
            if height[i] <= height[j]:
                max_area = max([max_area, (j-i)*height[i]])
                i += 1
                
            elif height[i] > height[j]:
                max_area = max([max_area, (j-i)*height[j]])
                j -= 1
                
        return max_area
        