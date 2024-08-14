print("*** multiplication or sum ***")
S1, S2 = map(int, input("Enter num1 num2 : ").split())
print("The result is ", end="")
if (S1 * S2 > 1000):
    print(S1+S2)
else:
    print(S1*S2)