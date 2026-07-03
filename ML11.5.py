# Write a program which accepts one number and checks whether it is palindrome or not.
# Input: 121
# Output: Palindrome

def main():
    No = int(input("Enter the number : "))
    Temp = No
    rev = 0

    while No > 0:
        Digit = No % 10
        rev = (rev * 10) + Digit
        No = No //10

    if Temp == rev:
        print("number is palindrome")

    else:
        print("Number is not palindrome")     

if __name__=="__main__":
    main()