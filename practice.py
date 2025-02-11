

# def is_palindrome(s):

#     rev = s.lower()

#     revs = rev[::-1]

#     if rev==revs:
#         return True
#     else:
#         return False
    
# print(is_palindrome("Madam"))   


def anagram(s,t):

    if len(s) != len(t):
        return False
    
    sort = sorted(s)

    sort1 = sorted(t)

    return sort == sort1
    

print(anagram("saurav" , "saruav"))