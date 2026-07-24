import schedule
import time
import shutil
import os
import datetime

def Backup():
    source = input("Enter source file path : ")
    destination = input("Enter destination directory path : ")

    filename = os.path.basename(source)
    name, extension = os.path.splitext(filename)

    current = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    backupfile = destination + "\\" + name + "_" + current + extension

    shutil.copy(source, backupfile)

    fileobj = open("backup_log.txt", "a")
    fileobj.write("Backup completed successfully at : " + str(datetime.datetime.now()) + "\n")
    fileobj.close()

    print("Backup completed successfully")

def main():
    print("Automation script started")

    schedule.every(1).hours.do(Backup)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()