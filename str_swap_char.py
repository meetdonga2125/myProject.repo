# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.




first_str = "Python"
sec_str = "Programming"

new_first_str = sec_str[:2] + first_str[2:]            # swap the first two character by index slicing..............
new_sec_str = first_str[:2] + sec_str[2:]


new_str = new_first_str + ' ' + new_sec_str
print("New string is: ", new_str)