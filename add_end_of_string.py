# Write a Python program to add 'ing' at the end of a given string (length
# should be at least 3). If the given string already ends with 'ing' then add
# 'ly' instead if the string length of the given string is less than 3, leave it
# unchanged.


lang = input("Enter a programming language: ")

if len(lang)>3 and  lang[-3:]!="ing":
    print(lang.replace(lang[-3:],"ing"))
    
elif len(lang)<3:
    print(lang)        
    
else:
   print(lang.replace(lang[-2:],"ly"))    