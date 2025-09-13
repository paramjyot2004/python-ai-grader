# Beginner Sample 1: Basic variable operations with common mistake
name = "Alice"
age = 20
print("Hello, my name is", name, "and I am", age, "years old")

# Student mistake: trying to concatenate string and integer
# greeting = "I am " + age + " years old"  # This will cause TypeError
# Correct version:
greeting = "I am " + str(age) + " years old"
print(greeting)
