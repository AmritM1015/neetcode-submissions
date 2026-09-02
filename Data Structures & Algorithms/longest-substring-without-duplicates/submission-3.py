class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initial Attempt
        # longest_seq = ""
        # curr_seq = ""
        # for char in s:
        #     if char not in curr_seq:
        #         curr_seq+=char
        #     else:
        #         if curr_seq[-1] == char:
        #             curr_seq = char
        #         if curr_seq[0] == char:
        #             curr_seq = curr_seq[1:] + char
        #     if len(curr_seq) > len(longest_seq):
        #         longest_seq = curr_seq
        # return len(longest_seq)
        
        # O(n^2) solution : takes too long
        # longest = 0
        # for i in range(len(s)):
        #     charSet = set()

        #     for j in range(i,len(s)):
        #         if s[j] in charSet:
        #             break
        #         charSet.add(s[j])
        #     longest = max(longest, len(charSet))
        # return longest
        
        charSet = set()
        l = 0
        r = 0
        result = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            result = max(result, r-l+ 1)
        return result
