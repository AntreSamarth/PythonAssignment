from multiprocessing import Pool
import os

def EvenSum(No):
    Sum = 0

    for i in range(2, No + 1, 2):
        Sum = Sum + i

    return (os.getpid(), No, Sum)

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    p = Pool()

    Result = p.map(EvenSum, Data)

    p.close()
    p.join()

    for value in Result:
        print("Process ID :", value[0])
        print("Input Number :", value[1])
        print("Sum of Even Numbers :", value[2])
        print()

if __name__ == "__main__":
    main()