class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        i=0
        while i<len(s):
            j=i
            while j<len(s):
                if(s[i:j+1] == s[i:j+1][::-1]):
                    count=count+1
                j=j+1
            i=i+1
        return count