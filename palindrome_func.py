# Write a Python function that checks whether a passed string is
# palindrome or no


def is_palindrome(word):
    if word == word[::-1]:
        print("I am a palindrome string")
    else:
        print("I am not a palindrome string")    

is_palindrome("aba")    
is_palindrome("abc")    
is_palindrome("atma")   
is_palindrome("malayalam") 
is_palindrome("atmta")

#Mehod-2----------------------------------------------------------

def ispalindrome(word):
    
    new_word = ""
    for i in word:
        new_word += i
        
    if (word==new_word):
        print("Yes")
    else:
        print("No")      
        
        
ispalindrome("xyz")     


#Metthod-3---------------------------------------------------------

def Ispalindrome(word):
    li_word = list(word)
    new_word = []
    new_word.extend(li_word)
    li_word.reverse()
    
    if(li_word==new_word):
        return True
    return False

print(Ispalindrome("aba"))
print(Ispalindrome("malayalam"))
print(Ispalindrome("Meet"))

        