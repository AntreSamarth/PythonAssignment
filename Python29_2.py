import os

def main():

    FileName = input("Enter file name : ")

    if(os.path.exists(FileName) == False):
        print("File does not exist")
        return

    fobj = open(FileName, "r")

    Data = fobj.read()

    print("Contents of file are :")
    print(Data)

    fobj.close()
