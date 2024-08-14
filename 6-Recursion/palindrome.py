def IsCheckColumn(text,begin,last):
    if begin == last:
        return True
    if text[begin] != text[last]:
        return False
    if begin < last+1:
        return IsCheckColumn(text,begin+1,last-1)
    return True

def Palindrome(str):
    n = len(str)
    if n == 0:
        return True
    return IsCheckColumn(str,0,n-1)

inp = input("Enter Input : ")
if Palindrome(inp):
    print(f"'{inp}' is palindrome")
else:    
    print(f"'{inp}' is not palindrome")