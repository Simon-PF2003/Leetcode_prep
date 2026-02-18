''' You are given an array of integers nums and an integer k. You must find the min length of a contiguous subarray of nums that sums to at least k. If there is no such subarray, 
return 0'''

def sum_k(nums, target):
    current_sum = 0
    left_pointer = 0
    min_length = float('inf')

    for right_pointer in range(len(nums)):
        current_sum += nums[right_pointer] #I add the current number to the sum
        while current_sum >= target: #If the sum is greater or equal to the target, I need to check if the length is the minimum, and I need to move the left pointer.
            min_length = min(min_length, right_pointer - left_pointer + 1)

            current_sum -= nums[left_pointer]
            left_pointer += 1
    
    return min_length if min_length != float('inf') else 0