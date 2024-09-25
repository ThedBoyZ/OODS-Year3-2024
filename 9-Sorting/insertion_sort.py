def insertion_sort(arr, n=None):
    if n is None:
        n = len(arr)
    if n <= 1:
        return arr
    
    insertion_sort(arr, n - 1)
    key = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > key:
        j -= 1
    
    print(f'insert {key} at index {j + 1} : {arr[:j + 1]} [{key}] {arr[j + 1:n - 1]}')
    arr.insert(j + 1, arr.pop(n - 1))

    return arr

input_data = input("Enter Input: ")
numbers = list(map(int, input_data.split()))

sorted_numbers = insertion_sort(numbers)

print("sorted")
print(sorted_numbers)
