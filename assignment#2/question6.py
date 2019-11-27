'''
Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are
less than 5.
'''

#empty list
numbers = []
n = int(input("How many number of sum you want: "))

#append user input in list
for i in range(n):
    number = int(input("Enter Number: "))
    numbers.append(number)

# cheaking numbers if lessthan 5 print it.
for i in range(n):
    if numbers[i] < 5:
        print(numbers[i])
