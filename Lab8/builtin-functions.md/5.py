def all_elements_true(input_tuple):
    return all(input_tuple)

def main():
    input_tuple = (True, True, True, True)
    result = all_elements_true(input_tuple)
    if result:
        print("All elements in the tuple are True.")
    else:
        print("Not all elements in the tuple are True.")

if __name__ == "__main__":
    main()
