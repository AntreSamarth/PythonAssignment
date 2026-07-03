# Write a program which accepts one number and prints count of digits in that number.
# Input: 7521
# Output: 4

def main():
    No = int(input("Enter the number : "))

    Count = 0

    while No > 0:
        Count = Count + 1
        No = No // 10

    print("Count of digits is : ",Count)    

if __name__=="__main__":
    main()
