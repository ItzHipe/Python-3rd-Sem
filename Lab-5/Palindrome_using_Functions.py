def is_palindrome(value):
    value_str = str(value)
    reversed_str = value_str[::-1]
    return value_str == reversed_str


print(is_palindrome("marram"))
print(is_palindrome("heya"))  
print(is_palindrome(12321))   
print(is_palindrome(12345))