import threading

def DisplayEven():
    print("First 10 Even Numbers:")
    for i in range(2, 21, 2):
        print(i)

def DisplayOdd():
    print("First 10 Odd Numbers:")
    for i in range(1, 20, 2):
        print(i)

def main():
    Even = threading.Thread(target=DisplayEven, name="Even")
    Odd = threading.Thread(target=DisplayOdd, name="Odd")

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

    print("Execution of main thread completed.")

if __name__ == "__main__":
    main()