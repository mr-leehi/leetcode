# 參考g2g的方法

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # transfer int to string
        # find reverse of the string
        # check if reverse and original are the same
        word = str(x)
        return word == word[::-1]