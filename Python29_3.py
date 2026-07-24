import sys
import os

def main():

    if(len(sys.argv) != 2):
        print("Usage : Python FileName.py ExistingFile")
        return

    if(os.path.exists(sys.argv[1]) == False):
        print("File does not exist")
        return

    Source = open(sys.argv[1], "r")
    Destination = open("Demo.txt", "w")

    Data = Source.read()

    Destination.write(Data)

    Source.close()
    Destination.close()

    print("Contents copied successfully")

if __name__ == "__main__":
    main()