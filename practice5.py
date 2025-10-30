# 1. Store following word meanings in a python dictionary: 
# table: "a piece of furniture", "list fo facts & figures" cat: "a small animal"

dictionary = {
    "table" : ["a piece of furniture", "list of facts & fugures"],
    "cat"   : "a small animal"

}

print(dictionary.get("table"))
print(dictionary.get("cat"))

# 2. You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students

sub_set = {"python","java","c++","python","javaScript","java","python","java","c++","c"}

print("The classroom needed = ", len(sub_set))

# 3. WAP to enter marks of 3 subjects from the user and store them in a dictionary . start with an empty dictionary and add one by one. use subject name as key and marks as value.

marks= {}

phy = int(input("Enter marks in physics: "))
marks["physics"] = phy

chem = int(input("Enter marks in chemistry: "))
marks["chemistry"] = chem

math = int(input("Enter marks in math: "))
marks["math"] = math



print(marks)


# Figure out a way to store 9 & 9.0  as separate values in the set . (You can take help of built - in data types)

value = {9,9.0, 9.25}
print(value)