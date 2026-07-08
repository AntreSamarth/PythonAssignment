import threading

def DisplayForward():
    print("Numbers from 1 to 50:")
    for i in range(1, 51):
        print(i)


def DisplayReverse():
    print("Numbers from 50 to 1:")
    for i in range(50, 0, -1):
        print(i)


def main():
    Thread1 = threading.Thread(target=DisplayForward, name="Thread1")
    Thread2 = threading.Thread(target=DisplayReverse, name="Thread2")

    Thread1.start()
    Thread1.join()      

    Thread2.start()
    Thread2.join()      

    print("Exit from main")


if __name__ == "__main__":
    main()