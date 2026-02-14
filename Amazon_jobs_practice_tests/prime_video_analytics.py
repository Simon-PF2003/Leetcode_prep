'''Amazon Prime Video wants to show a row of tendencies with the most popular categories of films users have been watching in Argentina.
You get a list of strings "categories" and an integer "k". Your task is to return a list of the "k" most popular categories. The order must be from the most popular to the 
least popular. If there are multiple categories with the same popularity, they should be ordered alphabetically.
The popularity of a category is determined by the number of times it appears in the list "categories". 
'''
#First NON SOLUTION (It didn't work because it doesn't order the categories with the same popularity alphabetically):
#The problem is that when I keep the heap's length as "k", I am not keeping all the categories with the same popularity. If action and comedy have the same popularity, 
#the heappushpop will keep the biggest category, which is comedy, and it will pop action. This way, I am not keeping all the categories with the same popularity, 
# and I am not ordering them alphabetically.
'''
def topKCategories(categories, k):
    result = []
    
    if categories is None or k <= 0:
        return result #If the input is invalid, I return an empty list.
    
    category_count = collections.Counter(categories) #I use a Counter to count the occurrences of each category in the list.
    heap = []

    for category, count in category_count.items():
        if len(heap) < k:
            heapq.heappush(heap, (-count, category)) #I push the count and the category into the heap. The heap will be ordered by count, and if there are multiple categories with the same count, they will be ordered by the order they were added to the heap.
        else:
            heapq.heappushpop(heap, (-count, category)) #If the heap has more than k elements, I push the new category and pop the least popular category. This way, I keep only the k most popular categories in the heap.
        
    while heap:
        count, category = heapq.heappop(heap) #I pop the categories from the heap. The count is positive, so I don't need to negate it.
        result.append(category)
    
    return result
    
    '''

#Second solution: It is less efficient, but it works because I keep all the categories with the same popularity in the heap, and I order them alphabetically. 
#When I append the result, it follows the heap's order. The time complexity is O(n log n) because of the sorting, and the space complexity is O(n) because of the heap.
import collections
import heapq

def topKCategories(categories, k):
    result = []

    if categories is None or k <= 0:
        return result #If the input is invalid, I return an empty list.
    
    category_count = collections.Counter(categories) #I use a Counter to count the occurrences of each category in the list.
    heap = [(-count, category) for category, count in category_count.items()] #I create a list of tuples with the count and the category. I use negative count because I want to use a min heap to get the most popular categories. 
    heapq.heapify(heap) #I convert the list into a heap. The heap will be ordered by count, and if there are multiple categories with the same count, they will be ordered alphabetically.
    for _ in range(min(k, len(heap))): #I iterate k times or the length of the heap, whichever is smaller, to get the k most popular categories. This way, if K is bigger than the length, I avoid an index error.
        count, category = heapq.heappop(heap) #I pop the most popular category from the heap. The count is negative, so I need to negate it to get the actual count.
        result.append(category)
    return result


if __name__ == "__main__":
    print(topKCategories(["Action", "Comedy", "Action", "Drama", "Comedy", "Action"], 2)) # ["Action", "Comedy"]
    print(topKCategories(["Horror", "Horror", "Comedy", "Action"], 3)) # ["Horror", "Action", "Comedy"]
    print(topKCategories(["Sci-Fi", "Sci-Fi", "Sci-Fi"], 1)) # ["Sci-Fi"]