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

    for value in Result:
        print("Process ID :", value[0])
        print("Input Number :", value[1])
        print("Factorial :", value[2])
        print()

if __name__ == "__main__":
    main()