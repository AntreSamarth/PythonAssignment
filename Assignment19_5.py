from functools import reduce

def ChkOdd(No):
    return No % 2 != 0

def Multiply(No):
    return No * 2

def Maximum(No1, No2):
    if No1 > No2:
        return No1
    else:
        return No2

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    print("Enter the elements:")
    for i in range(Size):
        No = int(input())
        Data.append(No)

    print("Input List:", Data)

    FData = list(filter(ChkOdd, Data))
    print("List after filter:", FData)

    MData = list(map(Multiply, FData))
    print("List after map:", MData)

    Result = reduce(Maximum, MData)
    print("Output of reduce:", Result)

if __name__ == "__main__":
    main()