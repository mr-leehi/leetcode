class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        lcp = ""   
        ki = 0
        s_index = 0
        s = strs[s_index]
        minlen = len(s)
        
        if len(strs) == 1:
            return strs[0]
        

        for i in range(len(strs)-1):
            
            if len(strs[i+1]) < minlen:
                minlen = len(strs[i+1])
                s_index = i+1
                s = strs[s_index]
                
    
        for j in range(minlen):
            
            if ki == 1:
                break
            
            lt = s[j]   
            a = 0
            
            for k in range(len(strs)):

                if k == s_index:
                    continue

                if lt != strs[k][j]:
                    ki = 1
                    break
                else:
                    a += 1

                if a == len(strs)-1:
                    lcp += lt
                
        return lcp
            
        