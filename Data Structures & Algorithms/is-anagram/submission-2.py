class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # D = {}
        # S = {}
        # for i in s:
        #     if i not in D:
        #         D[i] = 1
        #     else:
        #         D[i]+=1
        # for i in t:
        #     if i not in S:
        #         S[i] = 1
        #     else:
        #         S[i]+=1
        # if
        for i in s:
            if s.count(i) != t.count(i):
                return False
        return True
