def fibonacci(n):
    return n if n < 2 else fibonacci(n-1) + fibonacci(n-2)

    # Write your code here.

n = int(input())
print(fibonacci(n))
