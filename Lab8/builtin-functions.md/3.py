def is_palindrome(input_string):
    cleaned_string = ''.join(input_string.lower().split())
    return cleaned_string == cleaned_string[::-1]

def main():
    input_string = input("Enter a string: ")
    if is_palindrome(input_string):
        print(f"{input_string} is a palindrome.")
    else:
        print(f"{input_string} is not a palindrome.")

if __name__ == "__main__":
    main()
