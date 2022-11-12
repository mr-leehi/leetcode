class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach_idx = 0
        
        for i, num in enumerate(nums):
            
            if i > max_reach_idx:
                return False
            max_reach_idx = max(num+i, max_reach_idx)
            
        return True
   
   