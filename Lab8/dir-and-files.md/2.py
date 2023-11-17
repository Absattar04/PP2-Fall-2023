import os

def list_directories(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return directories

def list_files(path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return files

def list_all(path):
    all_entries = os.listdir(path)
    return all_entries

def main():
    path = input("Enter the path: ")
    directories = list_directories(path)
    print("Directories:", directories)
    files = list_files(path)
    print("Files:", files)
    all_entries = list_all(path)
    print("All Directories and Files:", all_entries)

if __name__ == "__main__":
    main()
