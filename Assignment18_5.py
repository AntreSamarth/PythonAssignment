import MarvellousNum

def ListPrime(Arr):
    Sum = 0

    for i in Arr:
        if MarvellousNum.ChkPrime(i):
            Sum = Sum + i

    return Sum

def main():
    Size = int(input("Enter number of elements:\n"))

    Data = []

    print("Enter the elements:")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ans = ListPrime(Data)

    print("Addition of prime numbers is:", Ans)

if __name__ == "__main__":
    main()