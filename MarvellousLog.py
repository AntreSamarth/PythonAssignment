import os
import time

def CreateLog(LogData):

    if(os.path.exists("Marvellous") == False):
        os.mkdir("Marvellous")

    CurrentTime = time.localtime()

    LogFileName = time.strftime("DuplicateRemovalLog_%d_%m_%Y_%H_%M_%S.log",CurrentTime)

    LogFileName = os.path.join("Marvellous",LogFileName)

    fobj = open(LogFileName,"w")

    fobj.write("Marvellous Duplicate File Removal Automation\n")
    fobj.write("-"*50+"\n")
    fobj.write("Starting Time : "+time.ctime()+"\n")
    fobj.write("-"*50+"\n\n")

    for Data in LogData:
        fobj.write(Data+"\n")

    fobj.write("\n")
    fobj.write("-"*50+"\n")
    fobj.write("Completion Time : "+time.ctime()+"\n")
    fobj.write("-"*50+"\n")

    fobj.close()

    return LogFileName