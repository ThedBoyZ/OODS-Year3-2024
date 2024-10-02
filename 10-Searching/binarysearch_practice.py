def bi_search(l, r, arr, x):
    if l == r:
        if arr[l] == x:
            return True
        else:
            False
    elif l > r:
        return False
    
    mid = (l+r)//2
    if arr[mid] > x:
        return bi_search(l, mid - 1, arr, x)

    elif arr[mid] < x:
        return bi_search(mid + 1, r, arr, x)
    else:
        return True # arr[mid] == x

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))