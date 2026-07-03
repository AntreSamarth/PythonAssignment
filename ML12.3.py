# Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.

def main():
    No1 = int(input("Enter the first number : "))
    No2 = int(input("Enter the second number : "))

    Add = No1 + No2
    Sub = No1 - No2
    Mul = No1 * No2
    Div = No1 / No2

    print("Addition is : ",Add)
    print("Substraction is : ",Sub)
    print("Multiplication is : ",Mul)
    print("Division is : ",Div)

if __name__=="__main__":
    main()