def Addition(Arr):
    Sum = 0

    for i in Arr:
        Sum = Sum + i

    return Sum

def main():
    Size = int(input("Enter the number of elements:\n"))

    Data = []

    print("Enter the elements:")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ans = Addition(Data)

    print("Addition of all elements is:", Ans)

if __name__ == "__main__":
    main()