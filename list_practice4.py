# WAP to ask the user to enter names of their 3 favorite movies and store them in a list.
movies = []
fav1 = input("Enter your favorite first movie name: ")
fav2 = input("Enter your favorite second movie name: ")
fav3 = input("Enter your favorite third movie name: ")

movies.append(fav1)
movies.append(fav2)
movies.append(fav3)

print(movies)


# WAP TO  check if a list contains a palindrome of elements.(Hints: use copy() method)

# Take input  as space - separated values
elements = input("Enter elements  separated by space: ").split()
print("List: ", elements)

# Make a copy of the list
copyList = elements.copy()

# Reverse the copied list 
copyList.reverse()

# check for palindrome 
if elements == copyList:
    print("List is palindrome")
else:
    print("List is not palindrome")



# WAP to count the number of students with the "A" grade in the following tuple.

grades = ("C","D","A","A","B","B","A")

count_A = grades.count("A")

print("The total number of A grade students is : ", count_A)

# store the above values in a list and store them frome "A" to " D"

grades_list = list(grades)
print(grades_list)

grades_list.sort()
print(grades_list)




