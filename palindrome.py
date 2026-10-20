def is_letter(char):
    if char >= 'A' and char <= 'Z' or char >= 'a' and char <= 'z':
            return True
    return False

# def is_palindrome(text):
#     text = text.lower()
#     left = 0
#     right = len(text) - 1

#     while left < right:
#         while left < right and not is_letter(text[left]):
#                 left += 1
#         while left < right and not is_letter(text[right]):
#                 right -= 1
#         if text[left] != text[right]:
#                 return False
#         left += 1
#         right -= 1

#     return True

def is_palindrome(text, left, right):
    text = text.lower()
    if left >= right:
        return True
    if not is_letter(text[left]):
        return is_palindrome(text, left + 1, right)  
    if not is_letter(text[right]):
        return is_palindrome(text, left, right - 1)
    if text[left] != text[right]:
        return False

    return is_palindrome(text, left + 1, right - 1)


# print(is_palindrome("Hello, World!"))                   # False
# print(is_palindrome("A man, a plan, a canal: Panama"))  # True
# print(is_palindrome("?!"))                              # True (no letters at all)
# print(is_palindrome(""))                                # True
# print(is_palindrome("ab"))                              # False

text = "Was it a car or a cat I saw?"
print(is_palindrome(text.lower(), 0, len(text) - 1))



    



