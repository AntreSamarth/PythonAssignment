import time
import schedule
import datetime

def Display():

    fileobj = open("Marvellous.txt", "a")

    fileobj.write("Task Executed at : " + str(datetime.datetime.now()) + "\n")

    fileobj.close()

    print("Task Executed")

def main():
    print("Automation script started")

    schedule.every(5).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()