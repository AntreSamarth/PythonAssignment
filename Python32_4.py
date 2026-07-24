import sys
import os
import time
import shutil
import schedule

def CopyFiles(Source, Destination):

    if(not os.path.isdir(Source)):
        print("Invalid Source Directory")
        return

    if(not os.path.isdir(Destination)):
        print("Invalid Destination Directory")
        return

    fobj = open("CopyLog.txt","a")

    for FolderName, SubFolder, FileNames in os.walk(Source):

        for fname in FileNames:

            if(fname.endswith(".txt")):

                SourceFile = os.path.join(FolderName,fname)

                try:
                    shutil.copy(SourceFile,Destination)
                    fobj.write(fname+" copied successfully\n")
                except:
                    fobj.write(fname+" cannot be copied\n")

    fobj.close()

def main():

    if(len(sys.argv) != 3):
        print("Usage : Python FileName.py Source Destination")
        return

    schedule.every(10).minutes.do(CopyFiles,sys.argv[1],sys.argv[2])

    CopyFiles(sys.argv[1],sys.argv[2])

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()