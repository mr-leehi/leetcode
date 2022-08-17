class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s_left = []
        
        for i in s:
            
            if i == '(' or i == '[' or i == '{':
                s_left.append(i)

            else:
                if s_left:
                    p = s_left.pop()
                    if i == ')' and p != '(':
                        return False
                    elif i == ']' and p != '[':
                        return False
                    elif i == '}' and p != '{':
                        return False

                else:
                    return False

        if s_left:
            return False
        else:
            return True

