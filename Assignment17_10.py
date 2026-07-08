def SumDigits(No):
    Sum = 0

    while No > 0:
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum

def main():
    Value = int(input("Enter number : "))

    Ret = SumDigits(Value)

    print("Addition of digits is :", Ret)

if __name__ == "__main__":
    main()