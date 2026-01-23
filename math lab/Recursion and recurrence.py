def factorial(n):
    if n == 0 or n == 1:          
        return 1
    return n * factorial(n - 1)
def fibonacci(n):
    if n == 0:                    
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
def power(base, exp):
    if exp == 0:                 
        return 1
    return base * power(base, exp - 1)
def gcd(a, b):
    if b == 0:                    
        return a
    return gcd(b, a % b)
# def recurrence(n):
#     if n == 0:                    
#         return 0
#     return recurrence(n - 1) + n
def recurrence(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total
def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:                    
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)

while True:
    print("1. Factorial of a number")
    print("2. Fibonacci sequence")
    print("3. Power of a number")
    print("4. GCD using Euclidean Algorithm")
    print("5. Evaluate recurrence T(n) = T(n-1) + n")
    print("6. Tower of Hanoi")
    print("7. Exit")

    choice = int(input("Enter your choice (1-7): "))

    if choice == 1:
        n = int(input("Enter a number: "))
        print("Factorial:", factorial(n))

    elif choice == 2:
        n = int(input("Enter number of terms: "))
        print("Fibonacci sequence:")
        for i in range(n):
            print(fibonacci(i), end=" ")
        print()

    elif choice == 3:
        base = int(input("Enter base: "))
        exp = int(input("Enter exponent: "))
        print("Result:", power(base, exp))

    elif choice == 4:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("GCD:", gcd(a, b))

    elif choice == 5:
        n = int(input("Enter value of n: "))
        print("T(n) =", recurrence(n))

    elif choice == 6:
        n = int(input("Enter number of disks: "))
        print("\nSteps to solve Tower of Hanoi:")
        tower_of_hanoi(n, "A", "B", "C")

    elif choice == 7:
        print("Stopped")
        break

    else:
        print("Invalid choice")
