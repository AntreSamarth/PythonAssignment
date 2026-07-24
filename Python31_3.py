import sys
import os
import time
import schedule

def DirectoryScanner(DirectoryName):

    if(os.path.isdir(DirectoryName) == False):
        print("Invalid Directory")
        return

    Files = 0
    Directories = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        Files = Files + len(FileName)
        Directories = Directories + len(SubFolder)

    print("-" * 40)
    print("Directory Scanned :", DirectoryName)
    print("Total Files :", Files)
    print("Total Subdirectories :", Directories)
    print("Scan Time :", time.ctime())
    print("-" * 40)

def main():

    if(len(sys.argv) != 2):
        print("Usage : Python FileName.py DirectoryName")
        return

    schedule.every(1).minute.do(DirectoryScanner, sys.argv[1])

    DirectoryScanner(sys.argv[1])

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()