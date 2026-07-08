import threading

def Maximum(Data):
    Max = Data[0]

    for No in Data:
        if No > Max:
            Max = No

    print("Maximum element is:", Max)


def Minimum(Data):
    Min = Data[0]

    for No in Data:
        if No < Min:
            Min = No

    print("Minimum element is:", Min)


def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    print("Enter the elements:")
    for i in range(Size):
        No = int(input())
        Data.append(No)

    T1 = threading.Thread(target=Maximum, args=(Data,), name="Thread1")
    T2 = threading.Thread(target=Minimum, args=(Data,), name="Thread2")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()