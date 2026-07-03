# Write a program which accepts one number and prints reverse of that number.
#Input: 123
#Output: 321

def main():
    No = int(input("Enter the number : "))

    rev = 0

    while No > 0:
        Digit = No % 10
        rev = (rev * 10) + Digit
        No = No //10

    print("Reverse number is : ",rev)    

if __name__=="__main__":
    main()    
    

