'''Amazon delivery drivers have "time windows" or "delivery blocks." Sometimes these blocks overlap, and we need to merge them to see the total time a driver is busy.
Problem:
Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the 
intervals in the input.'''

#input = intervals = [[1,3],[4,5],[2,4]]
def mergeIntervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        start_prev, end_prev = merged[-1]
        curr_start, curr_end = current

        if curr_start <= end_prev:
            merged[-1][1] = max(end_prev, curr_end)
        else: 
            merged.append(current)
    return merged

