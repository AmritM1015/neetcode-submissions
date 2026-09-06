class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda pair: pair[0]) # Sort based on starting index
        output = [intervals[0]]
        for start, end in intervals:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
        # initial attempt
        # new_intervals = []
        # for i in range(0, len(intervals)-1):
        #     if intervals[i+1][0] <= intervals[i][1]:
        #         new_intervals.append([intervals[i][0], intervals[i+1][1]])
        #     else:
        #         new_intervals.append(intervals[i+1])
        # return new_intervals