'''We have an array of integers minutes where each element represents the duration of a song played by a user in chronological order.
We need to find the maximum total listening time a user spent during any contiguous sequence of exactly k songs.'''


#Input: minutes = [1, 2, 3, 4, 5], target = 2
#Output: 9

def max_listening_time(minutes, k):
    if len(minutes) < k:
        return 0
    current_sum = sum(minutes[:k])
    max_sum = current_sum

    for i in range(k, len(minutes)): #I start from the k-th element because I already have the sum of the first k elements.
        current_sum += minutes[i] - minutes[i-k] #I add the current element and I subtract the element that is k positions behind, so I maintain the sum of the last k elements.
        max_sum = max(max_sum, current_sum)

    return max_sum
        