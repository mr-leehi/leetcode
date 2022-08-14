def binom(n, k):
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
          
        i = 1
        n_ways = 0
        
        if n%2 == 1:
            while n-i > i:
                n_ways += binom(n-i, i)
                i += 1
            return n_ways+1
            
        elif n%2 == 0:
            while n-i > i:
                n_ways += binom(n-i, i)
                i += 1
            return n_ways+2

            