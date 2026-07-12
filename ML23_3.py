from multiprocessing import Pool
import os

def EvenCount(No):
    Count = 0

    for i in range(2, No + 1, 2):
        Count = Count + 1

    return (os.getpid(), No, Count)

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    p = Pool()

    Result = p.map(EvenCount, Data)

    p.close()
    p.join()

    for value in Result:
        print("Process ID :", value[0])
        print("Input Number :", value[1])
        print("Even Number Count :", value[2])
        print()

if __name__ == "__main__":
    main()