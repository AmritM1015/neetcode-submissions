class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list)
        # for s in strs:
        #     sortedS = " ".join(sorted(s))
        #     res[sortedS].append(s)
        # return list(res.values())
        result = defaultdict(list) # Avoids edge case where list is not created

        for s in strs:
            count = [0] * 26 # each character a - z

            for char in s:
                count[ord(char) - ord("a")] += 1
            
            result[tuple(count)].append(s) # Lists cannot be keys so tuple is used
        
        return list(result.values()) # casting to a list is required