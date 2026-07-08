def NameLength(Name):
    return len(Name)

def main():
    Value = input("Enter name : ")

    Ret = NameLength(Value)

    print("Length of name is :", Ret)

if __name__ == "__main__":
    main()