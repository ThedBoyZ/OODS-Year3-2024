# n,s = [int(e) for e in input("Enter number and shiftcount : ").split()]
# print(n//(2**s))

print((lambda n, s: n // (2 ** s))(*map(int, input("Enter number and shiftcount : ").split())))
