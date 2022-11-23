#palindrom check 
#abcd #abcde

def is_palindrome(s:str):
    l= len(s)
    lim= int(l/2)
    for i in range(0, lim):
        # print(s[i], s[l-i-1])
        if s[i] != s[l-i-1]:
            return False
    return True 

def max_palindromic_substring(s:str):
    le= len(s)
    
    for i in range(le,0,-1):
        idx= 0 
        while idx+i <= le:
            print(s[idx:idx+i])
            if is_palindrome(s[idx:idx+i]):
                return (s[idx:idx+i], i)
            idx+=1 
s= 'cbbd'
print(max_palindromic_substring(s))