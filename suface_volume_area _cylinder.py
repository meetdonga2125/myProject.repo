# Write a Python program to calculate surface volume and area of a
# cylinder


pi = 22/7
radius = float(input("Enter a value of radius: ")) 
height = float(input("Enter a value of height: "))
sur_area = 2*pi*radius**2 + 2*pi*radius*height
volume = pi*radius**2*height
print(sur_area)
print(volume)