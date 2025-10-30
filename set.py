# set 
collection = {1,2,3,4,"hello ", "world"}
print(collection)
print(type(collection))
print(len(collection))

# duplicate value in set
duplicate_value = {1,2,2,2,"pranti","pranti"}
print("duplicate value = ", duplicate_value)

# Empty set
collection = {} # empty dictionary
print(type(collection))

collection = set()
print(type(collection))

# set method

# 1. set.add(el) ->add an element
element = set()

element.add(1)
element.add(2)
element.add(2)
element.add("hello")
element.add(False)
element.add((1,6,8))

print(type(element))
print(element)

# 2. set.remove(el) -> remove an element
element.remove(False)
print(element)

# 3. set.clear() -> empties the set
#element.clear()

# 4. set.pop() -> removes a random value
element.pop()
print(element.pop())
print(element)

# 5. set1.union(set2)
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7,8}

set_union = set1.union(set2)
print(set_union)

# 6. set1.intersect(set2)

set_intersect = set1.intersection(set2)
print(set_intersect)

print(set1)
print(set2)
