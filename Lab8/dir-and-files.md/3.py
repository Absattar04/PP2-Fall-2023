import os

def analyze_path(input_path):
    if os.path.exists(input_path):
        filename = os.path.basename(input_path)
        directory = os.path.dirname(input_path)

        print(f"Path exists.")
        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print("Path does not exist.")

def main():
    input_path = input("Enter the path to be analyzed: ")
    analyze_path(input_path)

if __name__ == "__main__":
    main()
