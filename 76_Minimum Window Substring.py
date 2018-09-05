class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #if len(s) < len(t) or not s or not t:
        #    return ''

        check = collections.Counter(t)
        l, r, i, j, need = 0, 0, 0, 0, len(t)

        while r < len(s):
            if check[s[r]] > 0:
                need -= 1
            check[s[r]] -= 1
            r += 1
            
            while need == 0:
                if j == 0 or (r - l) < (j - i):
                    i, j = l, r
                check[s[l]] += 1
                if check[s[l]] > 0:
                    need += 1
                l += 1

        return s[i:j]