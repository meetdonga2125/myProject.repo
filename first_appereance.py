# Write a Python program to find the first appearance of the substring
# 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
# whole 'not'...'poor' substring with 'good'. Return the resulting string.


word = "Mukesh ambani is not a poor man"
word1 = word.find("not")
# print(word1)                  index --> 17

word2 = word.find("poor")
# print(word2)                  index --> 23 

if word2>word1:                 # 23 > 17
    print(word.replace(word[word1:(word2+4)],'good'))           # word2+4 --->  17+4 == 21... 17,18,19,20......  21 doen't included


    