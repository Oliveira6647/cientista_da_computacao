def is_palindromo(s1):
    if s1.lower() == s1[::-1].lower():
        return True
    return  False


print(is_palindromo())