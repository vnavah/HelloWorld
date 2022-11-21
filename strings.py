print("Today is a good day to learn Python")
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world")
greeting = "Hello"
name = 'Vico'
print(greeting + name)

# if we want a space, we can add that to
print(greeting + " " + name)


age = 39
print(age)

print(type(greeting))
print(type(age))

age_in_words = "2 years"
print(name + " is " + str(age) + " years old")
print(name + f" is {age} years old")
print(f"{name} is {age} years old")
print(type(age_in_words))

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22/7
print(f"Pi is approximately {pi:12.50f}")

print("Done!")