class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        if (n<=0):
            return False
        log2 = math.log2(n)
        return (log2%1==0)