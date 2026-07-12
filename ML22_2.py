from multiprocessing import Pool
import os

def Factorial(No):
    Fact = 1

    for i in range(1, No + 1):
        Fact = Fact * i

    return (os.getpid(), No, Fact)

def main():
    Data = [10, 15, 20, 25]

    p = Pool()

    Result = p.map(Factorial, Data)

    p.close()
    p.join()

    print("Process ID\tInput Number\tFactorial")

    for value in Result:
        print(value[0], "\t\t", value[1], "\t\t", value[2])

if __name__ == "__main__":
    main()s