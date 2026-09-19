class Solution(object):
    def reverseWords(self, s):
        s=s.strip()
        words=s.split(" ")
        result=[]
        for word in words:
            if word !='':
                result.insert(0,word)
        return " ".join(result)        