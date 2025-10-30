# print numbers from 1 to 100

i = 1 
while i<=100:
    print (i)
    i += 1


# print numbers from 100 to 1.

i = 100 
while i>=1:
    print(i)
    i -=1



# print the multiplication table of a number n

n = int(input("Enter any number = "))

i = 1

while i<=10:
    print(n, "*", i, "=", i*n)
    i += 1


# print the elements of the following list using a loop:[1,4,9,16,25,36,49,64,81,100]

i =3
n = 1
square = []
square.append(n)

while n<100 :
    
    n = n+i
    square.append(n)
    i += 2

print(square)

# different way (traverse)
nums = [1,4,9,16,25,36,49,64,81,100]

i = 0
while i< len(nums):
    print(nums[i])
    i += 1
    
# search for a number x in this tuple using loop:

num = (1,4,9,16,25,36,49,64,81,100)

x = 36
i = 0
while i< len(nums):
    if(nums[i] == x):
        print("Found at index",i)
    
    i += 1
   