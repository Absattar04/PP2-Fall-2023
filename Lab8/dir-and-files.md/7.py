import shutil

def copy_file(source_file, destination_file):
    shutil.copy(source_file, destination_file)

def main():
    source_file_path = input("Enter the source file path: ")
    destination_file_path = input("Enter the destination file path: ")
    copy_file(source_file_path, destination_file_path)
    print(f"Contents of {source_file_path} copied to {destination_file_path} successfully.")

if __name__ == "__main__":
    main()