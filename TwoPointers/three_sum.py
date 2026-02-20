'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0."
The twist: El array NO está ordenado al principio.
No podés tener trillizos duplicados en el resultado.'''

def threeSum(nums):
    if not nums:
        return []
    nums.sort()
    right_pointer = len(nums) - 1
    res = [] 
    for i in range(nums):
        if nums[i] > 0:
            break
        if i>0 and nums[i] == nums [i-1]:
            continue

        left_pointer = i+1
        while left_pointer < right_pointer:
            current_sum = nums[i] + nums[left_pointer] + nums[right_pointer]
            if current_sum == 0:
                res.append([i, left_pointer, right_pointer])
                left_pointer += 1
                right_pointer -= 1
                while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer - 1]:
                    left_pointer += 1
                while left_pointer < right_pointer and nums[right_pointer] == nums[right_pointer + 1]:
                    right_pointer -= 1
            elif current_sum < 0:
                left_pointer += 1
            else:
                right_pointer -= 1 
    return res