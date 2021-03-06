class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def check(w):
            m1, m2 = {}, {}
            for x,y in zip(w,pattern):
                if x not in m1:m1[x]=y
                if y not in m2:m2[y]=x
                if (m1[x],m2[y])!=(y,x):
                    return False
            return True
        return list(filter(check,words))