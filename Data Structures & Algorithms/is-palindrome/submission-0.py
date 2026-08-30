import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lptr = 0
        rptr = len(s) - 1
        alphanum = string.ascii_letters + string.digits
        while( lptr <= rptr):
            if(s[lptr] not in alphanum):
                lptr+=1
                continue
            if (s[rptr] not in alphanum):
                rptr-=1
                continue
            if s[lptr].lower() != s[rptr].lower():
                return False
            lptr+=1
            rptr-=1

        return True
