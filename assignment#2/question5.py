#empty list
numbers = []
n = int(input("How many number of sum you want: "))

#append user input in list
for i in range(n):
    number = int(input("Enter Number: "))
    numbers.append(number)

print(max(numbers))
