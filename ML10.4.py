# Write a program which accepts one number and prints all even numbers till that number.
# Input: 10
# Output: 2 4 6 8 10

def main():
    No = int(input("Enter the number : "))

    for i in range(1, No + 1):
        if i % 2 == 0:
            print(i, end = " ")

if __name__== "__main__":
    main()

