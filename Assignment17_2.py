def Display(No):
    for i in range(No):
        for j in range(No):
            print("*", end="\t")
        print()

def main():
    Value = int(input("Enter number : "))

    Display(Value)

if __name__ == "__main__":
    main()
