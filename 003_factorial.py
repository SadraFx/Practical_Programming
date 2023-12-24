def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print("The factorial of" , n , "is :", fact)

factorial(5)   # > 120
factorial(10)  # > 3628800
factorial(20)  # > 2432902008176640000
