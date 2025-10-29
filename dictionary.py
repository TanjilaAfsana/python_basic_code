info = {
    
    "name": "apnacollege",
    "subjects" : ["python","machine learning","Artificial intelligent" ],
    "topics" : [ "disc","set"],
    "learning": "coding",
    "age" : 24,
    "is_adult" : True,
    "marks" : 94.4,
    1 : 2
}

# find type
print(type(info["subjects"]))

# individual value
print(info["subjects"])
print(info["learning"])
print(info["name"])

# change value
info["name"] = "pranti"

print(info)

# empty dictionary create

null_dict = {}
null_dict["name"] =" apnacollege"
print(null_dict)

# Nested Dictionaries

student = {
    "name" : "pranti",
    "subject": {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

print(student)
print(student["subject"]["phy"])

# length of dictionary
print("dictionary lenght",len(student))


# Dictionary method

# 1.student.keys() -> returns all keys

print("keys = ",student.keys())

# 2. student.values() -> returns all values
print("values = ",student.values())

# 3. student.items() -> returns all(key,value) pair as tuples
print("items = ",student.items())

# 4. student.get("key") -> returns the key according to value
print(student.get("subject"))

# 5. student.update(newDict) -> insert the specified items to the dictionary
student.update({"city": "delhi", "age ": 24})
print(student)