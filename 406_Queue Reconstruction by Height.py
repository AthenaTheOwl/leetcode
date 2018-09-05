class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        sp=sorted(people,key=lambda x: (x[0],-x[1]), reverse=True)
        result=[]
        for x in sp:
            result.insert(x[1],x)
        return result