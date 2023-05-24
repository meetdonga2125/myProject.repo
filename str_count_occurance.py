# Write a Python program to count occurrences of a substring in a string


ini_str = "xyzxyzxyzxyz"
sub_str = 'xyz'

count = 0
n = len(ini_str)                            # n = 12
m = len(sub_str)                            # m = 3

for i in range(n - m + 1):                  # n-m = 9+1   range(10)
	if ini_str[i:i+m] == sub_str:           #[0:0+3] == 'xyz'   ini_str[0:3] == 'xyz'
		count += 1                                              #index= 0,1,2 == 'xyz'

print("Number of substrings:", count)


#----------------------------------------------------------------------------------

indices = []
    # Start searching for the substring from the beginning of the string
start_index = 0
    # Continue searching until the substring is not found in the remaining part of the string
while True:
        # Find the next occurrence of the substring starting from the current start_index
        index = ini_str.find(sub_str, start_index)
        if index == -1:
            # If the substring is not found, break out of the loop
            break
        else:
            # If the substring is found, add its start index to the list of indices
            indices.append(index)
            # Update the start index to start searching for the next occurrence of the substring
            start_index = index + 1

print(indices)
    