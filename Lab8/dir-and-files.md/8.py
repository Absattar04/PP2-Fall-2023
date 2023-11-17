import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            os.remove(file_path)
            print(f"File {file_path} deleted successfully.")
        else:
            print(f"Permission denied: Unable to delete {file_path}.")
    else:
        print(f"The file {file_path} does not exist.")

def main():
    file_path = input("Enter the file path to be deleted: ")
    delete_file(file_path)

if __name__ == "__main__":
    main()
