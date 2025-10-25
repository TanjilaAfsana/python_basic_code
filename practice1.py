# write a program  to input 2 number and print their sum

num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))
sum = num1+num2
print("The total =", sum)

# WAP to input side of a square and print its area

side = float(input("Enter square side:"))

print("area = ", side*side)

# WAP to input 2 floating point numbers and print their average

num1 = float(input("Enter the first floating point: "))
num2 = float(input("Enter the second floating point: "))

avg = (num1+num2)/2
print("The Average number is =", avg)

# WAP to input 2 int numbers, a and b. print True if a is greater than or equal to b. if not print False.

a = int(input("Enter your a = "))
b = int(input("Enter your b = "))

if(a>=b):
    print(True)
else:
    print(False)
    