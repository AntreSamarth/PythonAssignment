class Numbers:

    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        Count = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                Count = Count + 1

        if Count == 2:
            return True
        else:
            return False

    def ChkPerfect(self):
        Sum = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum = Sum + i

        if Sum == self.Value:
            return True
        else:
            return False

    def Factors(self):
        print("Factors are : ", end="")

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")

        print()

    def SumFactors(self):
        Sum = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum = Sum + i

        return Sum


def main():

    No = int(input("Enter number : "))

    Obj = Numbers(No)

    if Obj.ChkPrime():
        print("Prime Number")
    else:
        print("Not Prime Number")

    if Obj.ChkPerfect():
        print("Perfect Number")
    else:
        print("Not Perfect Number")

    Obj.Factors()

    Ret = Obj.SumFactors()
    print("Sum of Factors :", Ret)


if __name__ == "__main__":
    main()