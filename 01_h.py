class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        r = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums), 1):
                if nums[i]+nums[j] == target:
                    break
            else:
                continue
            break
        r.append(i)
        r.append(j)
        return r