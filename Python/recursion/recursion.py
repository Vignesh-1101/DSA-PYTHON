def checkRecusion(n):
    if n == 1:
        print("n is 1")
    else:
        checkRecusion(n-1)
        print(n)

def factorial(n):
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)
    
def fib(n):
    if n in [0, 1]:
        print(n)
        return n
    else:
        print(n)
        return fib(n-1) + fib(n-2)
# fib(10)
    
def findmax(arr, n):
    if n == 1:
        print( arr[0])
    else:
        print(max(arr(n-1), findmax(arr, n-1)))

# checkRecusion(4)
# print(factorial(20))
# print(fib(4))

def reversenumvers(num):
    if num == 0:
        return num
    else:
        print(num-1)
        reversenumvers(num-1)

# print(reversenumvers(11))

def print_numbers(n, max_num):
    if n > max_num:
        return
    print(n)
    print_numbers(n + 1, max_num)
    print(n)

# Call the function
# print_numbers(1, 10)
def fibn(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibn(n-1) + fibn(n-2)
    
for i in range(10):
    print(fibn(i), end=" ")