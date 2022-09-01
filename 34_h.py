class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if not nums:
            return [-1, -1]
        
        if len(nums) == 1:       
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
              
                
        temp = 0
        
        for i in range(len(nums)):

            if nums[i] == target:
                while i+temp < len(nums):
                    if nums[i+temp] != target:
                        break
                    else:
                        temp += 1

                break     
                
            if i == len(nums)-1:
                return [-1, -1]
                
        return [i, i+temp-1]
        
        