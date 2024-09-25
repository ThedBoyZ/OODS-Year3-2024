def is_sorted(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True

input_data = input("Enter Input : ")
numbers = list(map(int, input_data.split()))

if is_sorted(numbers):
    print("Yes")
else:
    print("No")
