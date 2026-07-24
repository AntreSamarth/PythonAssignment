def CopyFile(source, destination):
    try:
        file1 = open(source, "r")
        file2 = open(destination, "w")

        for line in file1:
            file2.write(line)

        file1.close()
        file2.close()

        print("Contents of", source, "copied into", destination)

    except FileNotFoundError:
        print("Source file does not exist.")


def main():
    source = input("Enter the existing file name : ")
    destination = input("Enter the new file name : ")

    CopyFile(source, destination)


if __name__ == "__main__":
    main()