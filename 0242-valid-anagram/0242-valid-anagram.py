
class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        m1 = {}
        m2 = {}

    
        for ch in s:
            if ch in m1:
                m1[ch] += 1
            else:
                m1[ch] = 1

        
        for ch in t:
            if ch in m2:
                m2[ch] += 1
            else:
                m2[ch] = 1

      
        if m1 == m2:
            return True
        else:
            return False