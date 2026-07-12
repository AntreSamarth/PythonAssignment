from multiprocessing import Pool
import time

def SumPower(No):
    Sum = 0

    for i in range(1, No + 1):
        Sum = Sum + (i ** 5)

    return Sum

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    Start = time.time()

    p = Pool()

    Result = p.map(SumPower, Data)

    p.close()
    p.join()

    End = time.time()

    print("Results :")
    for i in range(len(Data)):
        print("N =", Data[i], "Sum =", Result[i])

    print("\nTotal Execution Time :", End - Start, "seconds")

if __name__ == "__main__":
    main()