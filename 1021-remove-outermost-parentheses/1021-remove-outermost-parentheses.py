class Solution(object):
    def removeOuterParentheses(self, s):
        result=""
        count=0
        for char in s:
            if char=='(':

                count+=1
                if count>1:

                    result+=char
            elif char==')':
                count-=1
                if count>0:
                    result +=char
        return result
        
        