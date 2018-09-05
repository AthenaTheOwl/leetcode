class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words=paragraph.lower().replace('!',' ').replace('?',' ').replace(',',' ').replace(';',' ').replace('.',' ').replace('\'',' ').split()
        count=0
        output=""
        i=0
        for word in words:
            if word not in banned:
                i=words.count(word)
                if i>count:
                    count=i
                    output=word
        return output