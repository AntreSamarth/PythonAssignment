import threading

def EvenList(Data):
    Even = []
    Sum = 0

    for i in Data:
        if i % 2 == 0:
            Even.append(i)
            Sum = Sum + i

    print("Even elements:", Even)
    print("Sum of even elements:", Sum)


def OddList(Data):
    Odd = []
    Sum = 0

    for i in Data:
        if i % 2 != 0:
            Odd.append(i)
            Sum = Sum + i

    print("Odd elements:", Odd)
    print("Sum of odd elements:", Sum)


def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    print("Enter the elements:")
    for i in range(Size):
        No = int(input())
        Data.append(No)

    T1 = threading.Thread(target=EvenList, args=(Data,), name="EvenList")
    T2 = threading.Thread(target=OddList, args=(Data,), name="OddList")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()