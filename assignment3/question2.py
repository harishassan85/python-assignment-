# Write a program to check if there is any numeric value in list using for loop

mylist = ['1', 'Sheraz', '2', 'Arain', '3', '4']
for item in mylist:
    mynewlist = [s for s in mylist if s.isdigit()]

print(mynewlist)
