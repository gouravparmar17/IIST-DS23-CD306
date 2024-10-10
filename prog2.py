# Write a program that takes two integer input a and b and swaps them using following
# techniques
# a. The third variable
# b. Arithmetic operators (Without using 3rd variable)
# c. XOR operator (Without using 3rd variable)
# d. Tuple packing and Unpacking (Pythonic Way)


a = int(input("Enter a number : "))
b = int(input("Enter a number : "))


# a. The third variable
# c = a
# a = b
# b = c

# b. Arithmetic operators (Without using 3rd variable)

# a = a + b
# b = a - b
# a = a - b

# c. XOR operator (Without using 3rd variable)

# a = a ^ b
# b = a ^ b
# a = a ^ b


# d. Tuple packing and Unpacking (Pythonic Way)

a, b = b, a

print(a, b)


