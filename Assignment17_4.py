def FactorsAddition(No):
    Sum = 0

    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i

    return Sum

def main():
    Value = int(input("Enter number : "))

    Ret = FactorsAddition(Value)

    print("Addition of factors is :", Ret)

if __name__ == "__main__":
    main()    