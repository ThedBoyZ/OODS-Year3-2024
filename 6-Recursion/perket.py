def select_ingredients(array, result_list=None, start=0, size=1):
    if start == len(array):
        return
    if not result_list:
        result_list = []
    if start + size <= len(array):
        result_list.append(array[start:start + size])
        select_ingredients(array, result_list, start, size + 1)
    else:
        select_ingredients(array, result_list, start + 1, 1)
    return result_list

def calculate(breads, y_sour, y_bitter, index=0):
    if index == len(breads) - 1:
        return breads[index][0], breads[index][1]
    sour, bitter = calculate(breads, y_sour, y_bitter, index + 1)
    return y_sour * sour * breads[index][0], y_bitter + bitter + breads[index][1]

def perket(bread_list_combinations, bread_list_index=0, min_difference=1000000001):
    if bread_list_index == len(bread_list_combinations):
        return min_difference
    y_sour, y_bitter = calculate(bread_list_combinations[bread_list_index], 1, 0)
    difference = abs(y_sour - y_bitter)
    using_difference = min_difference
    if difference <= min_difference:
        using_difference = difference
    min_difference = perket(bread_list_combinations, bread_list_index + 1, using_difference)
    return min_difference

input_data = [[int(i) for i in cook.split()] for cook in input("Enter Input : ").split(",")]
perket_combinations = select_ingredients(input_data)
print(perket(perket_combinations))