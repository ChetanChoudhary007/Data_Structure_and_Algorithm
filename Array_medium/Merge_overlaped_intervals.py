class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # declared the number of rows
        rows=len(intervals)

        # return list
        final_list=[]

        # main logic
        intervals.sort()

        for i in range(rows):

            # if the interval doesn't overlapped the last interval!!!
            if len(final_list)==0 or final_list[-1][1] < intervals[i][0]:
                final_list.append(intervals[i])

            #if the interval overlapped the last interval!!!
            else:
                final_list[-1][1]=max(final_list[-1][1], intervals[i][1])

        # return the final_list!!
        return final_list