class BankAccount:

    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder :", self.Name)
        print("Current Balance :", self.Amount)

    def Deposit(self):
        Money = float(input("Enter amount to deposit : "))
        self.Amount = self.Amount + Money

    def Withdraw(self):
        Money = float(input("Enter amount to withdraw : "))

        if Money <= self.Amount:
            self.Amount = self.Amount - Money
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest


def main():

    Obj1 = BankAccount("Samarth", 10000)

    Obj1.Display()

    Obj1.Deposit()
    Obj1.Display()

    Obj1.Withdraw()
    Obj1.Display()

    Ret = Obj1.CalculateInterest()
    print("Interest is :", Ret)

    print()

    Obj2 = BankAccount("Rahul", 5000)

    Obj2.Display()

    Obj2.Deposit()
    Obj2.Display()

    Obj2.Withdraw()
    Obj2.Display()

    Ret = Obj2.CalculateInterest()
    print("Interest is :", Ret)


if __name__ == "__main__":
    main()