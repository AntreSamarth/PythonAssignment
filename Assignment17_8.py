def Display(No):
    for i in range(1, No + 1):
        for j in range(1, i + 1):
            print(j, end="\t")
        print()

def main():
    Value = int(input("Enter number : "))

    Display(Value)

if __name__ == "__main__":
    main()