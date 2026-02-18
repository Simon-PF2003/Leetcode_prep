'''Given a string, return true if it is a palindrome, and false otherwise. Consider just alphanumeric characters and ignore uppercases and lowercases'''

def is_palindrome(words):
    if not words:
        return False
    words_modified = "".join(ch.lower() for ch in words if ch.isalnum())
    left_pointer = 0
    right_pointer = len(words_modified)-1
    while left_pointer < right_pointer:
        if words_modified[left_pointer] != words_modified[right_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1
    return True

if __name__ == '__main__':
    print(is_palindrome('A man, a plan, a canal: Panama'))   
    print(is_palindrome('Hello'))


