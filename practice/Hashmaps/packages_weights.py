'''At Amazon, we handle millions of packages. Imagine we have an array of integers representing the weights of packages in a delivery hub. We want to group these packages into 
pairs such that the sum of the weights of each pair is equal to a specific 'target' weight.
The Challenge:
Given an array of integers weights and an integer target, return the indices of the two numbers such that they add up to the target.
You may assume that each input would have exactly one solution.
You may not use the same element twice.
You can return the answer in any order.'''

def sumWeight(weights, target):
    dict_weights = {}
    for i, weight in enumerate(weights):
        complement = target - weight
        if complement in dict_weights:
            return [dict_weights[complement], i]
        dict_weights[weight] = i
    return []


# Test inputs
if __name__ == "__main__":
    print(sumWeight([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(sumWeight([3, 2, 4], 6))  # Output: [1, 2]
    print(sumWeight([3, 3], 6))  # Output: [0, 1]
    print(sumWeight([1, 5, 10, 20], 15))  # Output: [1, 2]

