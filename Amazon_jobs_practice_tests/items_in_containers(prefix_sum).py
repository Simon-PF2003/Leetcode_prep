'''Given a string s consistingitems as "*" and "|" as compartments walls; an array of startingIndices and an array of endingIndices, determine the number of items
in the compartments between the startingIndices and endingIndices, respectively.
Example: s = "|**|*|*", startingIndices = [1, 1], endingIndices = [5, 6]
The number of items in the compartments between the first pair of indices is 2, and the number of items in the compartments between the second pair of indices is 3. Return an 
array of integers representing the number of items in the compartments for each pair of indices. [2,3]'''

#First, I need to iterate through the string to know the number of items acumulated on each position. I can save this in a list. Then, to know where are the compartments and 
#compare them to the indices, I can save the position of the right and left walls in two lists. Finally, I can iterate through the indices and compare them with the walls
# to know how many items are between them. O(n) of time and O(n) of space.

def numberOfItems(s, startIndices, endIndices):
    length = len(s)
    items_acumulated = [0] * length #I create a list to save the number of items acumulated on each position.
    count = 0

    for i in range(length):
        if s[i] == '*':
            count += 1
        items_acumulated[i] = count #If the character is an item, I increase the count and I save it in the list.
    
    #Now I need to save the walls in two lists, one for the left walls and one for the right walls.
    left_walls = [-1] * length #I create a list to save the position of the left walls. I initialize it with -1, because the example indicates that index 0 is 1 in the indice
    last_wall = -1
    for i in range(length):
        if s[i] == '|':
            last_wall = i
        left_walls[i] = last_wall #If the character is a wall, I save its position in the list. If it is not a wall, I save the position of the last wall that I found.
    
    right_walls = [-1] * length #I create a list to save the position of the right walls. I initialize it with -1, because the example indicates that index 0 is 1 in the indice
    last_wall = -1
    for i in range(length-1, -1, -1):
        if s[i] == '|':
            last_wall = i
        right_walls[i] = last_wall #If the character is a wall, I save its position in the list. If it is not a wall, I save the position of the last wall that I found.
    
    results = []
    #Finally, I iterate through the indices and compare them with the walls to know how many items are between them.
    for start, end in zip(startIndices, endIndices):
        i, j = start - 1, end - 1 #I need to subtract 1 from the indices, because the example indicates that index 0 is 1 in the indices.
        left_wall = right_walls[i] #I get the position of the first wall going from the index to the right.
        right_wall = left_walls[j] #I get the position of the first wall going from the index to the left.

        if left_wall != -1 and right_wall != -1 and left_wall < right_wall:
            results.append(items_acumulated[right_wall] - items_acumulated[left_wall]) #If there are walls on both sides and the left wall is on the left of the right wall, I calculate the number of items between them and I add it to the results.
        else:
            results.append(0) #If there are no walls on one of the sides or the left wall is on the right of the right wall, it means that there are no items between them, so I add 0 to the results.
    return results

if __name__ == "__main__":
    print(numberOfItems("|**|*|*", [1, 1], [5, 6])) # [2,3]
    print(numberOfItems("*|*|", [1], [4])) # [1]
    print(numberOfItems("*|*|*", [1], [5])) # [1]