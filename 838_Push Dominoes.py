class Solution(object):

    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        force = [0]*len(dominoes)

        r = 0
        for i in xrange(len(dominoes)):
            if dominoes[i] == 'R':
                r = len(dominoes)
            elif dominoes[i] == 'L':
                r = 0
            else:
                r = max(r-1, 0)
            force[i] += r

        l = 0
        for i in reversed(xrange(len(dominoes))):
            if dominoes[i] == 'L':
                l = len(dominoes)
            elif dominoes[i] == 'R':
                l = 0
            else:
                l = max(l-1, 0)
            force[i] -= l

        return "".join('.' if f == 0 else 'R' if f > 0 else 'L'
                       for f in force)