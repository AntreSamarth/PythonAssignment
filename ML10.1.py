# Write a program which accepts one number and prints multiplication table of that number. 
# Input: 4 
# Output: 4 8 12 16 20 24 28 32 36 40

def main():
    No1 = int(input("Enter the Number : "))
    for i in range(1,11):
        print(No1 * i, end = " ")

if __name__== "__main__":
    main()

