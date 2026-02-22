'''Okay, let's look at a coding problem. I'm going to give you an array called nums which only contains 0s and 1s. I’m also giving you an integer k. Your goal is to
 find the maximum number of consecutive 1's in the array if you can flip at most k 0's to 1's.'''

#input = nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
#output = 10
def maxConsecutiveOnes(nums, k):
    if not nums or not k:
        return 0
    left_pointer = 0
    max_count = 0
    flip = 0

    for right_pointer in range(len(nums)):
        if nums[right_pointer] == 0:
            flip += 1
        
        while flip > k:
            if nums[left_pointer] == 0:
                flip -= 1
            left_pointer += 1
        max_count = max(max_count, right_pointer - left_pointer + 1)
    return max_count 