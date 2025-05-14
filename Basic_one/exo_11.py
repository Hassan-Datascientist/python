 #Python program to print the documents (syntax, description etc.) of Python built-in function(s).
def print_doc(function_name):
    func = __builtins__.__dict__.get(function_name)
    if func:
        print(f"{function_name}{func.__doc__}")
    else:
        print(f"Function '{function_name}' not found.")

# Example usage
print_doc('abs')
