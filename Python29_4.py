import sys
import os

def CompareFile(FileName1, FileName2):
    if os.path.isfile(FileName1) and os.path.isfile(FileName2):

        File1 = open(FileName1, "r")
        File2 = open(FileName2, "r")

        Data1 = File1.read()
        Data2 = File2.read()

        if Data1 == Data2:
            print("Success")
        else:
            print("Failure")

        File1.close()
        File2.close()

    else:
        print("One or both files do not exist.")

def main():
    if len(sys.argv) != 3:
        print("Usage: python Program.py <FileName1> <FileName2>")
        return

    CompareFile(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()