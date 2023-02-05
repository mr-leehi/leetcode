class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        
        idx = 0
        idx_max = len(haystack) - len(needle)
        
        while idx <= idx_max:
            
            if haystack[idx:idx+len(needle)] == needle:
                return idx
                
            idx += 1
            
        return -1
        
        