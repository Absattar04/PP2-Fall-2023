import time
import math

def square_root(num, ms):
    delay_sec = ms / 1000.0
    time.sleep(delay_sec)
    result = math.sqrt(num)
    return result

def main():
    num = int(input("Enter the number: "))
    ms = int(input("Enter the delay in milliseconds: "))
    result = square_root(num, ms)
    print(f"Square root of {num} after {ms} milliseconds is {result}")

if __name__ == "__main__":
    main()