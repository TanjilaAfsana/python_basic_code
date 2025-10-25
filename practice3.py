# WAP to check if a number entered by the user is odd or even.
num = int(input("Enter any integer number: "))

if(num%2 == 0):
    print("This is Even number:",num)
else:
    print("This is odd number : ", num)


# WAP To find the greatest of 3 numbers entered by the user.

num1 = int(input("Enter any number1 = "))
num2 = int(input("Enter any number2 = "))
num3 = int(input("Enter any number3 = "))


if(num1> num2 and num1>num3):
    print(num1," is the greatest")

elif(num2>num1 and num2> num3):
    print(num2,"is greatest number")

else:
    print(num3,"is greatest number")


# WAP to check if a number is a multiple of 7 or not.

num = int(input("Enter any number: "))

if(num%7 ==0):
    print(num ,"is a multiple of 7")
else:
    print(num,"is not multiple of 7")