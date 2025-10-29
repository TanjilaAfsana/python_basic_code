tup = (1,2,3,4)
print(tup)
print(type(tup))
print(tup[0])
print(tup[3])

# empty tuple
tup = ()
print(tup)

# single value tuple
tup = (1, )
print(tup)
print(type(tup))

tup =(1)
print(tup)
print(type(tup))

tup = ("hello",)
print(tup)
print(type(tup))

#.................... tuple slicing ......................
tup = (1,3,4,6,2)
print(tup[1:5])


# ----------------------Tuple Method ----------------------

tup = (2,1,3,1)

# tup.index(el) -> returns index of first occurrence tup.index(1) is 1

print(tup.index(1))

# tup.count(el) -> counts total occurrences tup.count(1) is 2

print(tup.count(1))
print(tup.count(2))


