# Traffic Lights Code

'''light = input("light color: ")
if(light == "red"):
     print("Stop")
elif(light == "green"):
     print("Go") 
elif(light == "yellow"):
     print("look")
else:
     print("light is broken")'''

# Grades of students

'''marks =int (input("marks: "))
if(marks>=90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C")
else:
    print("D")'''


# print output for: 1. A=5 & G = M 2. A = 2 & G=F
'''
A = int (input("A: "))
G = input("M/F: ")
if((A == 1 or A ==2)and G == "M"):
     print("fee is 100")
elif(A==3 or A == 4 or G == "F"):
     print("fee is 200")
elif(A == 5 and G == "M"):
     print("fee is 300")
else:
     print("no fee")
     '''

# single line if/ Ternary operator
'''food = input("food: ")
eat = "yes" if food == "cake" else "no"
print(eat)

food = input("food: ")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")'''
'''
age = int(input("age: "))
vote = ("yes", "no") [age>=18]
print(vote)'''

"""
sal = float(input("salary: "))
tax = sal*(.1, .2) [sal<=50000]
print(tax)
"""

# nesting

age = int(input("Enter your age: "))

if(age>=18):
    if(age>=80):
        print("cannto drive")
    else:
        print("can drive")
else:
    print("cannot drive your are",age)




