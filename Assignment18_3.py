def Minimum(Arr):
    Min = Arr[0]

    for i in Arr:
        if i < Min:
            Min = i

    return Min

def main():
    Number = int(input("Enter number of elements:\n"))

    Data = []

    print("Enter the elements:")

    for i in range(Number):
        Value = int(input())
        Data.append(Value)

    Ans = Minimum(Data)

    print("Minimum number is:", Ans)

if __name__ == "__main__":
    main()