class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # Stores pairs of temperatures and indices
        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((temp,i)) 
        return res


        # Initial Solution (Brute Force) - Time limit exceeded
        # s = []
        # j = 0

        # # Ok so we have a list of temperatures, and we need to know when the next day is for a warmer temperature.
        # # The hint says to use a stack, I guess one "brute force solution" we could do is keep track of the current temp and then see 
        # for i in range(len(temperatures)):
        #     j = i
        #     cur = j
        #     while j < len(temperatures)-1 and not temperatures[j] > temperatures[cur]:
        #         j+=1
        #     if temperatures[j] > temperatures[cur]:
        #         s.append(j-cur)
        #     else:
        #          s.append(0)
        # return s 
                