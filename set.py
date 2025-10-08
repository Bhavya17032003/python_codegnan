# TOPIC : SET

s = {10, 20, 30}
print(s)

#EXAMPLE 1 :

s = {1, 2, 3, 54, 60, (1, 2, 3), "codegnan", 1, 3}
print(s)


# null set:
s1 = {}
s2 = set()
print(type(s1), type(s2))

# set of integers from user

s = set(map(int, input().split()))
print(s)

s = set(map(int, input().strip().split()))
print(s)

# TOPIC 1 : SET OPERATIONS
# UNION # INTERSECTION # DIFF # SUPERSET # SYMMETRIC # DISjoint


# using methods and operators
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = {6, 7, 8}
s4 = {9}
print("union:", s1.union(s2))
print("intersection:", s1.intersection(s2))
print("difference:", s1.difference(s2))
print("symmetric difference:", s1.symmetric_difference(s2))
print("subset:", s1.issubset(s2))
print("superset:", s1.issuperset(s2))
print("disjoint:", s4.isdisjoint(s3))
print("disjoint:", s3.isdisjoint(s2))
print("union (s1 | s2):", s1 | s2)
print("intersection(s1 & s2):", s1 & s2)
print("difference (s1 - s2):", s1 - s2)
print("difference (s2 - s1):", s2 - s1)
print("symmetric(s1 ^ s2):", s1 ^ s2)
print("s2 is subset of s1:", s2 <= s1)
print("s2 is superset of s1:", s2 >= s1)
print("s1 and s3 disjoint:", (s1 & s3) == set())
print("s1 and s2 disjoint:", (s1 & s2) == set())

# MODIFICATION OPERATORS
# ADD, REMOVE, DISCARED, POP, UPDATE, CLEAR

s = {1, 2, 3, 4, 20, 15}
s.add(60)
print(s)
s.remove(20)
print(s)
s.discard(2)
print(s)
removed_s = s.pop()
print(s)
s.update({1, 2, 3})
print(s)
s.clear()
print(s)
















































































































































