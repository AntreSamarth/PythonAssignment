import sys
import os
import time
import schedule

import MarvellousChecksum
import MarvellousLog
import MarvellousMail

def DeleteDuplicate(DirectoryName):

    StartTime = time.ctime()

    Duplicate = MarvellousChecksum.FindDuplicate(DirectoryName)

    DeletedList = []

    TotalFiles = 0
    DuplicateFiles = 0
    DeletedFiles = 0

    for Key in Duplicate:

        TotalFiles = TotalFiles + len(Duplicate[Key])

        if(len(Duplicate[Key]) > 1):

            DuplicateFiles = DuplicateFiles + len(Duplicate[Key]) - 1

            for FileName in Duplicate[Key][1:]:

                os.remove(FileName)

                DeletedList.append(FileName)

                DeletedFiles = DeletedFiles + 1

    EndTime = time.ctime()

    LogFile = MarvellousLog.CreateLog(StartTime,
                                      EndTime,
                                      DirectoryName,
                                      TotalFiles,
                                      DuplicateFiles,
                                      DeletedFiles,
                                      DeletedList)

    SenderEmail = "yourgmail@gmail.com"
    SenderPassword = "Your_App_Password"
    ReceiverEmail = "receiver@gmail.com"

    Body = "Duplicate File Removal Process Completed Successfully."

    MarvellousMail.SendMail("antresamarth744@gmail.com",
                            "Samarth@123",
                            "antresamarth855@gmail.com",
                            LogFile,
                            Body)

    print("Duplicate files deleted successfully")

def main():

    Border = "-" * 40

    print(Border)
    print("Marvellous Automation Script")
    print(Border)

    if(len(sys.argv) != 2):
        print("Usage : Python DuplicateFileRemoval.py DirectoryName")
        return

    schedule.every(1).hours.do(DeleteDuplicate, sys.argv[1])

    DeleteDuplicate(sys.argv[1])

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()