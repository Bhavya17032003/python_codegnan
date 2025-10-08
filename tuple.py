# TOPIC : TUPLE

# WE CAN MENTION TUPLE WITH () AND TUPLE() FUNCTION

# LIST OF INTEGERS FROM USER :

t1 = ()
t2 = tuple()
t = tuple(map(int,input().split( )))
print(t)

# LIST OF STRINGS FROM USER  :

t1 = ()
t2 = tuple()
t = tuple(map(str,input().split()))
print(t)

t = [1, 2, 3]
tuple = input().split()
print(tuple)


#tuple is immutable :
 # single elemnt represntation 
t = (20)
t2 = (30)
print(type(t), type(t2))


# index / slicing:

t = (1, 2, 3, [10, 20, 30], "codegnan")
print(t[2], t[-2], t[-1])           # we are assigning value so using square brackets
print(t[-1:2:-1])
print(t[3:-4:-1])

# LIST OPERATIONS :

# 1. CONCATINATION

t1 = (1, 2, 3)
t2 = ('A', 'B')
print(t1 + t2)

# 2. REPETITION :

t1 = (1, 2, 3)
t2 = t1 * 3
print(t2)

#  TUPLE METHODS :

t = (1, 2, 3, [10, 20, 30], "codegnan")
ind = t.index(3)
count = t.count(1)
print(ind, count)

# BULITIN FUNCTIONS :
#len(), max(), min(), sum()

t = (1, 2, 3, 4, 5, 6)
print(len(t), max(t), min(t), sum(t))

# string in tuple conversion :

s = "codegnan"
print(list(s))
del s
s = "codegnan"
print(tuple(s))

# tuple to list converion

t = (1, 2, 3, 4, 5)
print(list(t))

