def CountWords(filename):
    file = open(filename, "r")

    count = 0

    for line in file:
        words = line.split()
        count = count + len(words)

    file.close()

    return count


def main():
    name = input("Enter the file name : ")

    result = CountWords(name)

    print("Total number of words in", name, ":", result)


if __name__ == "__main__":
    main()