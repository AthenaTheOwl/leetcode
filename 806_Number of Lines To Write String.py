class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        dist=0
        line=1
        for c in S:
            k=widths[(ord(c)-97)]
            if ((dist+k)<100):
                dist=dist+k
            elif ((dist+k)>100):
                line=line+1
                dist=k
            elif((dist+k)==100):
                dist=0
                line=line+1
        return [line,dist]