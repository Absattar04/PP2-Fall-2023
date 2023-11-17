def write_list_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print(f"List successfully written to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_path = input("Enter the path to the file: ")
    data_list = ["Apple", "Banana", "Orange", "Grapes"]
    write_list_to_file(file_path, data_list)

if __name__ == "__main__":
    main()
