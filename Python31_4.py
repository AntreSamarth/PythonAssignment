import time
import schedule

def CreateLog():

    CurrentTime = time.localtime()

    FileName = time.strftime("MarvellousLog_%d_%m_%Y_%H_%M_%S.txt", CurrentTime)

    fobj = open(FileName, "w")

    fobj.write("Log file created successfully.\n")
    fobj.write("Creation Time : ")
    fobj.write(time.strftime("%d-%m-%Y %I:%M:%S %p", CurrentTime))

    fobj.close()

    print(FileName, "created successfully")

def main():

    CreateLog()

    schedule.every(10).minutes.do(CreateLog)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()