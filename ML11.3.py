# Write a program which accepts one number and prints sum of digits.
# Input: 123
# Output: 6

def main():
    No = int(input("Enter the number : "))

    Sum = 0

    while No > 0:
        Digit  = No % 10
        Sum =  Sum + Digit
        No = No // 10 

    print("Sum of digits are : ",Sum)    

if __name__=="__main__":
    main()