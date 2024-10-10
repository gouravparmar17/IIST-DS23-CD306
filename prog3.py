# 3 program in Python that takes an integer input n and prints wether it is even or
# odd using following techniques
# a. Simple If Else statement
# b. Without using % operator
# c. Without using == operator


n = int(input("Enter a number : "))


# a. Simple If Else statement

if n % 2 == 0: print(n, "is even")
else: print(n, "is odd")


# b. Without using % operator

if (n // 2) * 2 == n: print(n, "is even")
else: print(n, "is odd")

# c. Without using == operator

arr = ["even", "odd"]
print(n, "is", arr[n % 2])