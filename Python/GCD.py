def gcd(n, m):
    if m == 0:
        return n
    else :
        return gcd(m, n%m)
    
print(gcd(48, 17))
