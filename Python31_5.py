import sys
import os
import time
import schedule

def DirectoryCount(DirectoryName):

    if(os.path.isdir(DirectoryName) == False):
        print("Invalid Directory")
        return

    Count = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        Count = Count + len(FileName)

    fobj = open("DirectoryCountLog.txt", "a")

    fobj.write("Directory Path : " + DirectoryName + "\n")
    fobj.write("Number of Files : " + str(Count) + "\n")
    fobj.write("Date and Time : " + time.ctime() + "\n")
    fobj.write("-" * 40 + "\n")

    fobj.close()

    print("Total Files :", Count)

def main():

    if(len(sys.argv) != 2):
        print("Usage : Python FileName.py DirectoryName")
        return

    schedule.every(5).minutes.do(DirectoryCount, sys.argv[1])

    DirectoryCount(sys.argv[1])

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()