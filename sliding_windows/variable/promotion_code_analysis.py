'''Amazon is analyzing customer search strings to find specific promotion codes. A promotion code is considered 'valid' if it is a Nice Subarray.
A Nice Subarray is a contiguous subarray that contains exactly k odd numbers.
Given an array of integers nums and an integer k, return the number of Nice Subarrays.'''

#input = [1, 1, 2, 1, 1], k = 3 output = 2 because the subarrays [1, 1, 2, 1] and [1, 2, 1, 1] are the only ones that contain exactly 3 odd numbers.
#  
def count_at_most(nums, k):
    if k < 0:
        return 0
    
    left_pointer = 0
    result = 0

    for right_pointer in range(len(nums)):
        if nums[right_pointer] % 2 != 0: #If the current number is odd, I decrease k because I need to find exactly k odd numbers.
            k -= 1
        while k < 0: #If k is less than 0, it means that I have found more than k odd numbers, so I need to move the left pointer until I have exactly k odd numbers again.
            if nums[left_pointer] % 2 != 0: #If the number at the left pointer is odd, I increase k because I am moving the left pointer and I am removing an odd number from the subarray.
                k += 1
            left_pointer += 1
        
        result += right_pointer - left_pointer + 1 #I add the number of subarrays that end at the right pointer and have exactly k odd numbers, which is the length of the current subarray.
    return result

def count_nice_subarrays(nums, k):
    return count_at_most(nums, k) - count_at_most(nums, k - 1) #The number of subarrays that have exactly k odd numbers is equal to the number of subarrays that have at most k odd numbers minus the number of subarrays that have at most k - 1 odd numbers.

if __name__ == "__main__":
    print(count_nice_subarrays([1, 1, 2, 1, 1], 3)) # 2
    print(count_nice_subarrays([2, 4, 6], 1)) # 0
    print(count_nice_subarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2)) #16