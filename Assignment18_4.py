def Frequency(Arr, No):
    Count = 0

    for i in Arr:
        if i == No:
            Count = Count + 1

    return Count

def main():
    Size = int(input("Enter number of elements:\n"))

    Data = []

    print("Enter the elements:")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Search = int(input("Enter the number to search:\n"))

    Ans = Frequency(Data, Search)

    print("Frequency of", Search, "is:", Ans)

if __name__ == "__main__":
    main()