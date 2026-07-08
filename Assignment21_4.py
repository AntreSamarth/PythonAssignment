import threading

Sum = 0
Product = 1

def SumList(Data):
    global Sum

    for No in Data:
        Sum = Sum + No


def ProductList(Data):
    global Product

    for No in Data:
        Product = Product * No


def main():
    global Sum, Product

    Data = []

    Size = int(input("Enter number of elements: "))

    print("Enter the elements:")
    for i in range(Size):
        No = int(input())
        Data.append(No)

    T1 = threading.Thread(target=SumList, args=(Data,), name="Thread1")
    T2 = threading.Thread(target=ProductList, args=(Data,), name="Thread2")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Sum of elements:", Sum)
    print("Product of elements:", Product)

    print("Exit from main")

if __name__ == "__main__":
    main()