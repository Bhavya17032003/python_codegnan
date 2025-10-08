# 1. split() : it returns list

s = "The Sky is Blue and ocean is Blue"
print(s.split())
print(s.split("Blue"))
print(s.split('u'))
print(s.split('z'))


# 2. sep.join() :

l = ['The', 'sky', 'is', 'blue', 'and', 'ocean', 'is', 'blue']
print("_".join(l))
print("".join(l))
print("@".join(l))

# NOTE : # chr() - it returns character of ASCII number
         # ord() -  it returns ASCII value of character

print(ord("A"))
print(chr(65))
print(chr(128514))

#3. string checking functions
# islower() - It returns True, when entire string is lower case
# isupper() - It returns True, when entire string is upper case
# isalpha()- It returns True, when entire string is only characters
# isalnum()- It returns True, when entire string is characters or digits
# istitle()- It returns True, when entire string is title case
# isdigit() - It returns True, when entire string is digits

print("Codegnan".islower())
print("codegnan".islower())
print("codegnan".isalpha())
print("codeGnan".isalnum())
print("CODEGNAN".isupper())
print("123".isalnum())
print("Codegnan".istitle())
print("codegnan1234".isdigit())
print("1723".isdigit())

# 4. string comparison
s1 = "abcd"
s2 = "abcde"
print(s1 == s2)
print(s1 > s2)
print(s1 < s2)
print("ABC" < "abc")

# 5. identity string comparision
s1 = "abcd"
s2 = "abcd"
print(id(s1), id(s2))
print(s1 == s2)
print(s1 is s2)

y# 6. bulit in functions :

# len() - it returns the length of string
print(len("codegnan"))
print(max("codegnan"))
print(min("codegnan"))

# replace() - it returns the replaced sub_string
s = "codegnan"
print(s.replace('o','1', 2))
print(s.replace('n', '2', 1)) # replaces n=old with new sub_string    

