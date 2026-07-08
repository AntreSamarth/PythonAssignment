import Arithmetic

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    print("Addition is :", Arithmetic.Add(Value1, Value2))
    print("Subtraction is :", Arithmetic.Sub(Value1, Value2))
    print("Multiplication is :", Arithmetic.Mult(Value1, Value2))
    print("Division is :", Arithmetic.Div(Value1, Value2))

if __name__ == "__main__":
    main()