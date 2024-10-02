def find_first_greater_value(left, right):
    min = []
    right.sort()  # เรียงลิสต์ด้านขวาเพื่อให้การค้นหาทำได้ง่ายขึ้น
    for val in right:
        found = False
        for r_val in left:
            if r_val > val:
                min.append(r_val)
                found = True
                min_greater_value = r_val
        for n in min:
            if min_greater_value > n and val < n:
                min_greater_value = n
        if found:
            print(f"{min_greater_value}")
        if not found:
            print(f"No First Greater Value")

inp = input('Enter Input : ').split('/')
left , right =  list(map(int, inp[0].split())), list(map(int, inp[1].split()))
find_first_greater_value(left, right)