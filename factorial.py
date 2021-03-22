def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial (n - 1) 
m = factorial(5)
print(m)
"""n = int(input("Enter Number : "))
if(n<0):
    print("Number should be greater than 0")
else:
    print("factorial of", n ,"is",factorial(n))"""
