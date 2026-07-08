def CountDigits(No):
    Count = 0

    while No > 0:
        Count = Count + 1
        No = No // 10

    return Count

def main():
    Value = int(input("Enter number : "))

    Ret = CountDigits(Value)

    print("Number of digits is :", Ret)

if __name__ == "__main__":
    main()