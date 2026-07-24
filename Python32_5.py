import sys
import os
import time
import schedule

def DeleteEmptyFiles(DirectoryName):

    if(not os.path.isdir(DirectoryName)):
        print("Invalid Directory")
        return

    fobj = open("DeleteLog.txt","a")

    for FolderName, SubFolder, FileNames in os.walk(DirectoryName):

        for fname in FileNames:

            FilePath = os.path.join(FolderName,fname)

            try:
                if(os.path.getsize(FilePath) == 0):
                    os.remove(FilePath)
                    print(FilePath,"Deleted")
                    fobj.write(FilePath+" Deleted\n")

            except PermissionError:
                print("Permission Denied :",FilePath)

    fobj.close()

def main():

    if(len(sys.argv) != 2):
        print("Usage : Python FileName.py DirectoryName")
        return

    schedule.every(1).hours.do(DeleteEmptyFiles,sys.argv[1])

    DeleteEmptyFiles(sys.argv[1])

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()