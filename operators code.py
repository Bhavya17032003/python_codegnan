print("# TOPIC 1 : arithemetic operator")

num1 = int(input())
num2 = int(input())
print("addition", num1 + num2)
print("subraction", num1 - num2)
print("multiplication", num1 * num2)
print("division", num1 / num2)
print("floor division", num1 // num2)
print("modulus", num1 % num2)
print("exponential", num1 ** num2)


print("# TOPIC 2 : assignment operator")

num = int(input())
print(num)
num += 5 #num = num + 5
print(num)
num -= 3
print(num)
num *= 2
print(num)
num /= 4
print(num)
num %= 3
print(num)
num **= 2
print(num)
num //= 2
print(num) 

print("#TOPIC 3 : comparison operator")

num1 = 10
num2 = 5
print("num1 == num2:", num1 == num2)
print("num1 != num2:", num1 != num2)
print("num1 > num2:", num1 > num2)
print("num1 < num2:", num1 < num2)
print("num1 >= num2:", num1 >= num2)
print("num1 <= num2:", num1 <= num2)

print("# TOPIC 4 : logical operator")
        
num1 = 10
num2 = 20
print("num1 > 5 and num2 > 10 :", num1 > 5 and num2 > 10)
print("num1 > 5 or num2 < 10 :", num1 > 5 or num2)
print("not(num1 > 5) :", not(num1 > 5))
print("not(num2 > 25) :", not(num2 > 25))


print("# TOPIC 5 : bitwise operator")
print("# TOPIC 5.1 : decimal to decimal")
num1 = 10
num2 = 4
print("num1 &num2 =", num1 & num2)  #1010 & 0100 = 0000
print("num1 | num2 =", num1 | num2) # 1010 | 0100 = 1110
print("num1 ^ num2 =", num1 ^ num2) # 1010 ^ 0100 = 1110
print("~num1 =", ~num1)             #~1010 = -(1010+1) = -(1011)
print("num1 << 1 =", num1 << 1)     #1010 << 1 = 10100
print("num1 >> 1 =", num1 >> 1)     #1010 >> 1 = 0101


print("# TOPIC 6 : arrows")
print("\u2190")
print("\u2191")
print("\u2192")
print("\u2193")
#left Arrow =\u2190
#up Arrow =\u2191
#right Arrow = \u2192
#down Arrow = \u2193

print("# TOPIC 5.2 : decimal to binary")

num = 10
print("Decimal:", num, "\u2192 Binary:", bin(num))

print("# TOPIC 5.3 : binary to decimal")

binary_num = "1010"
decimal_num = int(binary_num, 2)
print("Binary:", binary_num, "\u2192 Decimal:", decimal_num)

print("# NOTE :")
print("\n ===int(binary_num, 2) - converts binary to decimal===")
print("\n===bin(decimal_number) - converts decimal to binary===")

print("# TOPIC 6 : membership operator ")

num = [1, 2, 3, 4, 5, 6]
print(3 in num)
print(8 in num)
print(10 not in num)
print("a" in "apple")
print("b" not in "apple")

print("# TOPIC 7 : Identity operator")

print("# Example 1: Same Object")
a = [1, 2, 3]
b = a   # b refers to the same object as a

print(a is b)       # True → both point to same memory
print(a is not b)   # False

print("# ex 2 : Different Objects, Same Values")
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)   # True → values are equal
print(x is y)   # False → different memory locations

print("# Example 3: Integers (Caching in Python) small / large")

m = 10
n = 10

print(m is n)   # True → small integers are cached by Python

m = 1000
n = 1000
print(m is n)   # False → larger integers may not be cached

print("# ✅ Summary : ")

print("# is - checks if two variables point to the same object.")

print("# is not - checks if they point to different objects.")

print("# == - checks values only.")


