# Write a program which accepts one number and prints binary equivalent.

def main():
    No = int(input("Enter the number : "))

    Binary = " "

    while No > 0:
        Digit = No % 2
        Binary = str(Digit) + Binary
        No = No // 2

    print("Binary equivalent is : ",Binary)    


if __name__=="__main__":
    main()