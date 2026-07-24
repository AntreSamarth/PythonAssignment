import os

def main():

    FileName = input("Enter file name : ")
    String = input("Enter string : ")

    if(os.path.exists(FileName) == False):
        print("File does not exist")
        return

    fobj = open(FileName, "r")

    Data = fobj.read()

    Count = Data.count(String)

    print("Frequency of", String, "is", Count)

    fobj.close()

if __name__ == "__main__":
    main()