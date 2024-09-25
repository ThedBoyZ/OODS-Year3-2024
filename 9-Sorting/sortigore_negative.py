def sort_positive(numbers):
    positive_numbers = [num for num in numbers if num >= 0]
    negative_numbers = [num for num in numbers if num < 0]
    
    for i in range(len(positive_numbers)):
        for j in range(0, len(positive_numbers) - i - 1):
            if positive_numbers[j] > positive_numbers[j + 1]:
                positive_numbers[j], positive_numbers[j + 1] = positive_numbers[j + 1], positive_numbers[j]

    result = []
    pos_index = 0
    for num in numbers:
        if num >= 0:
            result.append(positive_numbers[pos_index])
            pos_index += 1
        else:
            result.append(num)
    
    return result

input_data = input("Enter Input : ")
numbers = list(map(int, input_data.split()))

sorted_numbers = sort_positive(numbers)
print(' '.join(map(str, sorted_numbers)))
