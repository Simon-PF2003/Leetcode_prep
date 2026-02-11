'''You are fiven a number n. For every integer i from 1 to n, print:
"Fizz" if i is a multiple of 3.
"Buzz" if i is a multiple of 5.
"FizzBuzz" if i is a multiple of both 3 and 5.
i if i is not a multiple of 3 or 5.'''
# First solution: I can use if / elif to check the multiples of 3 and 5. 
# Efficient, but if I need many conditions, it is not very scalable. 
# O(n) of time and O(1) of space.
'''def fizzBuzz(n):
    # Write your code here
    for i in range(1, n+1):
        if i%3 == 0 and i%5 == 0:
            print('FizzBuzz')
        elif i%3 == 0:
            print('Fizz')
        elif i%5 == 0:
            print('Buzz')
        else:
            print(i)'''

#Second solution: I can avoid if / elif by creating a dictionary with the multiples and their corresponding strings.
# This is less efficient, but more scalable. If I want to add more multiples, I just need to add them to the dictionary.
#  O(n) of time and O(1) of space.

def fizzBuzz(n):
    dict_fizzbuzz = {3: 'Fizz', 5: 'Buzz'}
    for i in range(1, n+1):
        output = ''
        for key in dict_fizzbuzz:
            if i%key == 0:
                output += dict_fizzbuzz[key]
        print(output or i)
if __name__ == "__main__":
    fizzBuzz(15)