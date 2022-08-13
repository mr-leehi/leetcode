class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        num = 0
        s += 'A'   
        
        while i < len(s)-1:
            
            if s[i] != 'A':
                   
                if s[i] == 'I':
                    num += 1
                    if s[i+1] == 'V':
                        num += 3
                        i += 1
                    elif s[i+1] == 'X':
                        num += 8
                        i += 1

                elif s[i] == 'V':
                    num += 5
                    
                elif s[i] == 'X':
                    num += 10
                    if s[i+1] == 'L':
                        num += 30
                        i += 1
                    elif s[i+1] == 'C':
                        num += 80
                        i += 1

                elif s[i] == 'L':
                    num += 50
                    
                elif s[i] == 'C':
                    num += 100
                    if s[i+1] == 'D':
                        num += 300
                        i += 1
                    elif s[i+1] == 'M':
                        num += 800
                        i += 1

                elif s[i] == 'D':
                    num += 500
                    
                elif s[i] == 'M':
                    num += 1000
                    
                i += 1
                
            else:
                break
                
        return num