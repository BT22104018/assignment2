variable1 = str(input('\n'))
print(len(variable1))
print(variable1[::-1])
sliced = slice(10,26)
print(variable1[sliced])
replacement = variable1.replace("a case sensitive","an object oriented")
print(replacement)
result = variable1.index(" a ")
print(result)
whitespace = " "
variable2 = ""
for char in variable1:
    if char != whitespace:
        variable2 = variable2 + char
print(variable2)