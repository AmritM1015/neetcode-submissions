class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Ok so this is a sliding window problem in a sense, we have "k" as len(s1)
        # We go through s2 and store the elements in an array keeping a left index and removing that leftmost index after moving to the next element
        # but we are comparing permutation, so I think maybe a hashmap is what we need
        cur_store = {}
        if len(s1) > len(s2):
            return False
        for c in s1:
            cur_store[c] = 1 + cur_store.get(c, 0)
        
        need = len(cur_store)
        for i in range(len(s2)): #idr exactly the looping range from last time tbh (nvm I was not correct there)
            count2, cur = {},0
            for j in range(i,len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j],0) # I keep forgetting to do this instead of how I initialize dictionaries
                if cur_store.get(s2[j],0) < count2[s2[j]]: # basically if the inner loop dictionary has something cur_store doesnt we break loop
                    break
                if cur_store.get(s2[j],0) == count2[s2[j]]: # If we have a correct character matching between the dicts we increment cur
                    cur+=1
                if cur == need:
                    return True
        return False