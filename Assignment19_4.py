from functools import reduce

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    print("Enter the elements:")
    for i in range(Size):
        No = int(input())
        Data.append(No)

    print("Input List:", Data)

    # Filter even numbers
    FData = list(filter(lambda No: No % 2 == 0, Data))
    print("List after filter:", FData)

    # Calculate square of each even number
    MData = list(map(lambda No: No ** 2, FData))
    print("List after map:", MData)

    # Add all squared numbers
    if len(MData) > 0:
        Result = reduce(lambda A, B: A + B, MData)
        print("Output of reduce:", Result)
    else:
        print("No even numbers found.")

if __name__ == "__main__":
    main()