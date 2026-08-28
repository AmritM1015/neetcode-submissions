class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS,countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1+countS.get(s[i],0)
            countT[t[i]] = 1+countT.get(t[i],0)
        return countS == countT

        # for i in t:
        #     if i not in S:
        #         S[i] = 1
        #     else:
        #         S[i]+=1
        # if
        # for i in s:
        #     if s.count(i) != t.count(i):
        #         return False
        # return True
