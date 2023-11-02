def extract_min_until_zero(array):
    min_element = float('inf')  
    for num in array:
        if num == 0:
            return min_element
        elif num < min_element:
            min_element = num
    return -1  

input_array = [123, 200, 0, 10, 0, 9, 1]
result = extract_min_until_zero(input_array)
print(result)