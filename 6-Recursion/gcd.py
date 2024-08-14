def find_gcd(x,y):
    while(y):
        x,y = y,x % y
    
    if x > 0:
        return x
    if x < 0:
        return (x*-1)
    
List_num = input("Enter Input : ").split(" ")
num1 = int(List_num[0])
num2 = int(List_num[1])

# Function GCD
gcd = find_gcd(num1, num2)
if (num1 == 0) and (num2 == 0):
    print("Error! must be not all zero.")
elif num1 > num2:
    print(f"The gcd of {num1} and {num2} is : {gcd}")
else:
    print(f"The gcd of {num2} and {num1} is : {gcd}")    
