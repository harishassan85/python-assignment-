'''
Write a program which takes 5 inputs from user for different subject’s
marks, total it and generate mark sheet using grades ?
'''

sub1 = int(input(f"Enter english marks: "))
sub2 = int(input(f"Enter math marks: "))
sub3 = int(input(f"Enter urdu marks: "))
sub4 = int(input(f"Enter Islamiyat marks:"))
sub5 = int(input(f"Enter Science marks: "))
   
sum = sub1+sub2+sub3+sub4+sub5
print(f"Your Total Marks of All Subjects is: {sum} ")
per = 100*sum/500
print(f"Your percentage is: {per} ")

if per >= 80 and per <= 100:
    print("Grade A")
elif per >= 70 and per <80:
    print("Grade B")
elif per >= 60 and per < 70:
    print("Grade C")
elif per >= 50 and per < 60:
    print("Grade D")
elif per >= 40 and per < 50:
    print("Grade E")
else:
    print("fail")
