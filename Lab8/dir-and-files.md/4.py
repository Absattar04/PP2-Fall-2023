def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
            return line_count
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_path = input("Enter the path to the text file: ")
    line_count = count_lines(file_path)

    if line_count is not None:
        print(f"The number of lines in the file is: {line_count}")

if __name__ == "__main__":
    main()
