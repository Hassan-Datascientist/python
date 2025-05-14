# Python program that accepts an integer (n) and computes the value of n+nn+nnn.
n = input("Enter an integer: ")
n1 = n + n
n2 = n + n + n
result = int(n) + int(n1) + int(n2)
print("The value of n+nn+nnn is:", result)
