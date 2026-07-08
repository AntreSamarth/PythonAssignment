import threading

def Small(String):
    Count = 0

    for ch in String:
        if ch.islower():
            Count = Count + 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Number of lowercase characters:", Count)
    print()


def Capital(String):
    Count = 0

    for ch in String:
        if ch.isupper():
            Count = Count + 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Number of uppercase characters:", Count)
    print()


def Digits(String):
    Count = 0

    for ch in String:
        if ch.isdigit():
            Count = Count + 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Number of digits:", Count)
    print()


def main():
    Value = input("Enter a string: ")

    T1 = threading.Thread(target=Small, args=(Value,), name="Small")
    T2 = threading.Thread(target=Capital, args=(Value,), name="Capital")
    T3 = threading.Thread(target=Digits, args=(Value,), name="Digits")

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

    print("Exit from main")


if __name__ == "__main__":
    main()