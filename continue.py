# continue statement: 
# The continue keyword is used to end the current iteration in a loop(For or while), and coutinues to the next iteration


n = int(input("Enter a num: "))

for i in range(n):
    if(i%2==0):                  #skip the iteration if the varible i is devided by 2
        continue
    print(i)