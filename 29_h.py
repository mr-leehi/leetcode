class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
                     
        if dividend == 0:
            return 0
        
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            if dividend // divisor > 2**31-1:
                return 2**31-1
            else:
                return dividend // divisor
        else:
            if dividend < 0:
                return -((-dividend) // divisor)
            elif divisor < 0:
                return -(dividend // (-divisor))

                