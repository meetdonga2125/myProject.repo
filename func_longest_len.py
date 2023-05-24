# Write a Python function that takes a list of words and returns the length
# of the longest one.



# def long_len():
    
#     len_list = ["Python", "Java", "Golang", "Android", "Javascript", "Python_django"]
    
#     for i in len_list:
#         print(i)
        
        
# long_len()      


def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["Fronted", "Backend", "Python_django", "Javascript", "Python", "Java"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])
  
  
