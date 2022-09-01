class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0

        for i in range(len(s)):

            templen = 0
            temp = 1

            while i+temp < len(s):

                if s[i+temp] in s[i:i+temp]:
                    break

                templen += 1
                temp += 1

            templen += 1    

            if templen > maxlen:
                maxlen = templen
                
        return maxlen
    
    