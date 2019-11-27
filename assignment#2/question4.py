#Write a Python program to sum all the numeric items in a list?

#initializing veriable sum
sum = 0

#empty list
numbers = []
n = int(input("How many number of sum you want: "))

#append user input in list
for i in range(n):
    number = int(input("Enter Number: "))
    numbers.append(number)

#sum of user input
for i in range(n):
    sum += numbers[i]

print(sum)