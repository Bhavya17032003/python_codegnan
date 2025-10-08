# TOPIC : LIST

cart = ["milk", "bread", "eggs"]
print(cart)

l = [1, 2, 3, [6, 5, 4]]
print(l[1])
print(l[-1])
print(l[0])

# LIST OPERATORS :
# 1 : CONCATENATION (JOIN 2 LISTS)
l1 = [1, 2, 3]
l2 = [3, 5]
print(l1 + l2)
12123

# 2: REPETITION (REPEATS LIST ELEMNTS)

lst = [0]
print(0 * 10)

# 3: INDEXING AND SLICING ([] - ACCESS ELEMENTS BY INDEX, [:] - GET SUBLISTS)

a = [10, 20, 30]
print(a[1])
print(a[0:2])

# 4: membership operator

# 5: IDENTITY OPERATOR

# 6: MAP() / SPLIT(): (TO READ LIST STRING int,string,

l = map(int,input().split())
print(l)

# TO READ LIST OF INTEGERS FROM USER

lst = list(map(int,input().split(',')))
print(lst)

# # TO READ LIST OF STRINGS FROM USER

lst = list(map(str,input().split(',')))
print(lst)


i = [1, 2, 3, 4]
i.append(10)
print("After Append 10:",i)
i.extend([20,30,40])
print("After Extend operation:",i)
i.insert(2,60)
print("after insert operation:",i)

# sorted():
nums = [3, 1, 2, 4]
new_nums = sorted(nums)
print(nums, new_nums)

# len(), max(), min(), sum():

lst = [1, 2, 5, 20, 15, 32,40]
print(len(lst), max(lst), min(lst), sum(lst))
lst = ["code", "bannu", "codegnan", "akky"]
print(len(lst), max(lst), min(lst))

# SINGLE ELEMNT ADD TO A LIST(lst):
l = [1, 2, 3, 4]
ele = 10
print(l + [ele])

