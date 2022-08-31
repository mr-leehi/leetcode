class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if abs(x) < 10:
            return x
        
        lst = list(str(x))
        lst.reverse()
        
        if x < 0:
            lst.pop()
            
        while lst:
            
            if lst[0] != "0":
                break
            else:
                lst.pop(0)
                
        rs = "".join(lst)
        if x < 0:
            if -int(rs) >= -2**31:
                return -int(rs)
            return 0
        
        elif x > 0:
            if int(rs) <= 2**31-1:
                return int(rs)
            return 0
        
        