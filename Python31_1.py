import time
import schedule

def DisplayMessage(Message):

    print(Message)

def main():

    Message = input("Enter message : ")
    Interval = int(input("Enter interval in seconds : "))

    if(Interval <= 0):
        print("Invalid interval")
        return

    schedule.every(Interval).seconds.do(DisplayMessage, Message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()