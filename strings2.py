#                   1
#         012345678901234
parrot = "Norwegian Blue"

print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,123;245:647 432,234;876"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
print("Done!")
