class Solution(object):
    def numSpecialEquivGroups(self, A):
        answer = set()
        for string in A:
            tmp = list(string)
            a, b = tmp[::2], tmp[1::2]
            answer.add((''.join(sorted(a)), ''.join(sorted(b))))
        return len(answer)