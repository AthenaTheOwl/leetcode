class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        if (n<=0):
            return False
        log3=(math.log10(n))/(math.log10(3))
        return (log3%1==0)