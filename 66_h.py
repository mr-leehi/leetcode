class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits_str = [str(i) for i in digits]
        s = "".join(digits_str)
        n_plus_one = int(s) + 1
        
        new_digits = ",".join(str(n_plus_one))
        
        return new_digits.split(",")