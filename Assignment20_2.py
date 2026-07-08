import threading

def EvenFactor(No):
    Sum = 0

    print("Even factors are:")
    for i in range(1, No + 1):
        if No % i == 0:
            if i % 2 == 0:
                print(i)
                Sum = Sum + i

    print("Sum of even factors:", Sum)


def OddFactor(No):
    Sum = 0

    print("Odd factors are:")
    for i in range(1, No + 1):
        if No % i == 0:
            if i % 2 != 0:
                print(i)
                Sum = Sum + i

    print("Sum of odd factors:", Sum)


def main():
    Value = int(input("Enter a number: "))

    T1 = threading.Thread(target=EvenFactor, args=(Value,), name="EvenFactor")
    T2 = threading.Thread(target=OddFactor, args=(Value,), name="OddFactor")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()