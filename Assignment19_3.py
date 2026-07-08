from functools import reduce

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    print("Enter the elements:")
    for i in range(Size):
        No = int(input())
        Data.append(No)

    print("Input List:", Data)

    FData = list(filter(lambda No: No >= 70 and No <= 90, Data))
    print("List after filter:", FData)

    MData = list(map(lambda No: No + 10, FData))
    print("List after map:", MData)

    Result = reduce(lambda A, B: A * B, MData)
    print("Output of reduce:", Result)

if __name__ == "__main__":
    main()