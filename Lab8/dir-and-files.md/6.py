import os

def generate_text_files():
    current_directory = os.getcwd()
    for char in range(ord('A'), ord('Z') + 1):
        file_name = f"{chr(char)}.txt"
        file_path = os.path.join(current_directory, file_name)
        with open(file_path, 'w') as file:
            file.write(f"This is the content of {file_name}")
    print("Text files created successfully.")

def main():
    generate_text_files()

if __name__ == "__main__":
    main()