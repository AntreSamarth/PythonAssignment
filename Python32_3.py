import sys
import os
import time
import schedule

def DisplayFile(FileName):

    if(os.path.exists(FileName) == False):
        print("Error : File does not exist")
        return

    if(os.path.isfile(FileName) == False):
        print("Error : It is not a file")
        return

    try:
        if(os.path.getsize(FileName) == 0):
            print("Error : File is empty")
            return

        fobj = open(FileName, "r")

        Data = fobj.read()

        print("-" * 40)
        print("Contents of file")
        print("-" * 40)

        print(Data)

        fobj.close()

    except PermissionError:
        print("Error : Permission denied")

    except OSError:
        print("Error : File cannot be opened")

def main():

    Border = "-" * 40

    print(Border)
    print("Marvellous Automation Script")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script reads and displays the contents of a text file every minute.")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage : Python FileName.py FileName")

        else:

            schedule.every(1).minute.do(DisplayFile, sys.argv[1])

            DisplayFile(sys.argv[1])

            while True:
                schedule.run_pending()
                time.sleep(1)

    else:
        print("Invalid number of arguments")
        print("Use --h or --u for more information")

    print(Border)
    print("Thank you for using Marvellous Automation Script")
    print(Border)

if __name__ == "__main__":
    main()