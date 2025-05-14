#Python program that accepts a filename from the user and prints the extension of the file


filename = input("Enter a filename: ")
file_extension = filename.split(".")[-1]
print("The extension of the file is:", file_extension)
