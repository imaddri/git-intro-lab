def fact(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
print(f" {fact(num)}")
print(f" {fact(num)}")
