import time
import schedule

def Lunch():
    print("Lunch Time!")

def WrapUp():
    print("Wrap up work")

def main():
    print("Automation script started")

    schedule.every().day.at("13:00").do(Lunch)
    schedule.every().day.at("18:00").do(WrapUp)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()