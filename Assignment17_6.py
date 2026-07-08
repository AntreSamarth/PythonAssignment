def Display(No):
    for i in range(No, 0, -1):
        for j in range(i):
            print("*", end="\t")
        print()

def main():
    Value = int(input("Enter number : "))

    Display(Value)

if __name__ == "__main__":
    main()