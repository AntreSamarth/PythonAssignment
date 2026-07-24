def CheckWord(filename, word):
    try:
        file = open(filename, "r")

        found = False

        for line in file:
            words = line.split()

            if word in words:
                found = True
                break

        file.close()

        return found

    except FileNotFoundError:
        return None


def main():
    name = input("Enter the file name : ")
    word = input("Enter the word to search : ")

    result = CheckWord(name, word)

    if result == None:
        print("Unable to open file.")
    elif result == True:
        print(word, "is found in", name)
    else:
        print(word, "is not found in", name)


if __name__ == "__main__":
    main()