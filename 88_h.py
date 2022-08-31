class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1
        
        for i in range(len(nums1)):
            
            if nums2 and m == 0:
                for j in range(len(nums2)):
                    nums1[-1-j] = nums2[-1-j]
                    
            else:
                if nums1[i] > nums2[0]:
                    nums1[i+1:i+1+m] = nums1[i:i+m]
                    a = nums2.pop(0)   
                    nums1[i] = a

                    if not nums2:
                        break

                else:
                    m -= 1
            
        return nums1

        