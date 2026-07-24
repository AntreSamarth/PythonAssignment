import time
import schedule

def CreateFile():

    CurrentTime = time.localtime()

    FileName = time.strftime("File_%d_%m_%Y_%H_%M_%S.txt", CurrentTime)

    fobj = open(FileName, "w")

    fobj.write("Filename : " + FileName + "\n")
    fobj.write("Creation Date : " + time.strftime("%d/%m/%Y", CurrentTime) + "\n")
    fobj.write("Creation Time : " + time.strftime("%H:%M:%S", CurrentTime) + "\n")

    fobj.close()

    print(FileName, "created successfully")

def main():

    Border = "-" * 40

    print(Border)
    print("Marvellous Automation Script")
    print(Border)

    CreateFile()

    schedule.every(1).minute.do(CreateFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

    print(Border)
    print("Thank you for using Marvellous Automation Script")
    print(Border)

if __name__ == "__main__":
    main()