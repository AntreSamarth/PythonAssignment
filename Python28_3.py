def DisplayFile(filename):
    file = open(filename, "r")

    for line in file:
        print(line, end="")

    file.close()


def main():
    name = input("Enter the file name : ")

    DisplayFile(name)


if __name__ == "__main__":
    main()