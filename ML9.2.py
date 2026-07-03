def ChkGreater():
    No1 = int(input("Enter the first number : "))
    No2 = int(input("Enter the second number : "))

    if No1 > No2:
        print(No1,"is greater")

    else:
        print(No2,"is greater")  

def main():
    ChkGreater()

if __name__=="__main__":
    main()