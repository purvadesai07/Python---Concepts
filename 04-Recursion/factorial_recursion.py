def factorial(n):
    if n == 0 or n == 1 :
        return 1
    else:
        return n*factorial(n-1)
n = int(input("Enter The Factorial Number: "))
result = factorial (n)
if result is None:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {n} is {result}")