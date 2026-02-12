'''Given an integer array of item weights, divide the item weights into two boxes, A and B, while respecting these conditions:
The intersection of A and B is null.
The union of A and B is the set of all item weights.
The number of elements in subset A is minimal.
The sum of the weights in subset A is greater than the sum of the weights in subset B.
Return the subset A in increasing order where the sum of A's weights is greater than the sum of B's weights. If there are multiple solutions, 
return the one with the smallest sum of weights in A.'''

#I can sort the weights in decreasing order, and I can keep adding weights to box A until the sum of A is greater than half the total.
def minimalHeaviestSetA(arr):
    arr.sort(reverse=True) #Sort in decreasing order.

    total_weight = sum(arr) #Calculate the total weight.
    target = total_weight / 2 #Calculate the target weight for box A, which is half of the total weight.
    box_a = [] 
    weight_a = 0

    for weight in arr:
        box_a.append(weight) #I add the weight to box A.
        weight_a += weight 
        if weight_a > target:
            break
    box_a.sort()
    return box_a

if __name__ == "__main__":
    print(minimalHeaviestSetA([3, 7, 5, 6, 2])) # [6,7]
    print(minimalHeaviestSetA([4, 4, 7, 6, 7])) # [6,7]