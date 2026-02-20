'''Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
Return the indices of the two numbers, [index1, index2].'''

def two_sum_ii(numbers, target):
    if not numbers:
        return []
    left_pointer = 0
    right_pointer = len(numbers)-1

    while left_pointer < right_pointer:
        if numbers[left_pointer] + numbers[right_pointer] == target:
            return [left_pointer+1, right_pointer+1]
        elif numbers[left_pointer] + numbers[right_pointer] < target:
            left_pointer += 1
        else: 
            right_pointer -= 1 
    return []    