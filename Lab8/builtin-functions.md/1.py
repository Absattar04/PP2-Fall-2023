from functools import reduce

def multiply_all(nums):
    result = reduce(lambda x, y: x * y, nums, 1)
    return result

def main():
    num_list = [1, 2, 3, 4, 5, 6]
    result = multiply_all(num_list)
    print(f"The product of all numbers in the list is: {result}")

if __name__ == "__main__":
    main()