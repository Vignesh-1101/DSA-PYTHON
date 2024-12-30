def decimalToBinary(n):
    assert int(n) == n, 'must be positive integer'
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimalToBinary(int(n/2))
        # return 0 + 10 * decimalToBinary(5)
        # return 1 + 10 * decimalToBinary(2)
        # return 0 + 10 * decimalToBinary(1)
        # return 1 + 10 * decimalToBinary(0)
    

print(decimalToBinary(10))