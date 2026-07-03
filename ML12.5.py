# Write a program which accepts one number and prints that many numbers in reverse order.
# Input: 5
# Output: 5 4 3 2 1

def main():
    No = int(input("Enter the Number : "))

    for i in range(No, 0, -1):
        print(i,end = " ",)

if __name__=="__main__":
    main()