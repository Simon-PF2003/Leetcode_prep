''' You are given an array of products weights sorted in ascending order. We want to find two products which sum is exactly equal to a target.'''

#Suppose just one solution
def warehouse_weights(weights, target):
    if len(weights) < 2 or target < 2: 
        return 0

    left_pointer = 0
    right_pointer = len(weights) - 1
    while left_pointer < right_pointer:
        current_sum = weights[left_pointer] + weights[right_pointer]
        if current_sum > target:
            print('menor', left_pointer, right_pointer, current_sum)
            right_pointer -= 1
        elif current_sum < target:
            print('mayor', left_pointer, right_pointer, current_sum)
            left_pointer += 1
        else:
            print('igual', left_pointer, right_pointer, current_sum)
            return [left_pointer, right_pointer]
    return []

#Suppose more than one solution
def warehouse_weights(weights, target):
    if len(weights) < 2 or target < 2: 
        return 0
    res = []
    left_pointer = 0
    right_pointer = len(weights) - 1
    while left_pointer < right_pointer:
        current_sum = weights[left_pointer] + weights[right_pointer]
        if current_sum > target:
            print('menor', left_pointer, right_pointer, current_sum)
            right_pointer -= 1
        elif current_sum < target:
            print('mayor', left_pointer, right_pointer, current_sum)
            left_pointer += 1
        else:
            print('igual', left_pointer, right_pointer, current_sum)
            res.append([left_pointer, right_pointer])
            left_pointer += 1
            right_pointer -= 1
    if res:
        return res
    return []

if __name__ == '__main__':
    print(warehouse_weights([2,7,11,15],9)) #[0,1]
