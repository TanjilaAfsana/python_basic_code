marks1 = 94.4
marks2 = 87
marks3 = 95
marks4 = 66
marks5 = 45

marks = [94.4, 87.5, 95.2,66.4,24.1]
print(marks)
print(len(marks))
print(type(marks))
print(marks[0])
print(marks[1])

student = ["karan", 94.5, "Delhi"]
print(student)
student[0]="Arjun"
print(student)

str = "hello"
print(str[0])
#str[0]="y"    # immutable -> error dibe

# list slicing

marks = [ 85, 94, 76,63,48]
print(marks[:4])
print(marks[1:])


# List Method

list = [2,1,3]

# list.append(value) ->mutable
list.append(4)
print(list)

# list.sort()

list.sort()
print(list)

# list.sort(reverse = True)
list.sort(reverse=True)
print(list)

# list.reverse

list = ["a",'d','e','f','c','b']
list.reverse()
print(list)

# list.insert(idx,element) -> insert element at index
list = [ 2 ,1 ,3]
list.insert(5,5)
list.insert(2,10)
print(list)

# list.remove -> remove first occurrence of element []

list = [2,1,3,1]
list.remove(1)
print(list)

# list.pop(idx) -> removes element at idx
list = [2,3,6,8,3]
list.pop(3)
print(list)